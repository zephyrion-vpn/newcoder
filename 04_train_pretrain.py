import argparse
import math
from pathlib import Path

import numpy as np
import sentencepiece as spm
import torch
from tqdm import tqdm

from model import GPT, GPTConfig


def get_batch(data, batch_size, block_size, device):
    max_start = len(data) - block_size - 1
    if max_start <= 0:
        raise ValueError("Dataset too small for selected block_size")
    ix = torch.randint(max_start, (batch_size,))
    x = torch.stack([torch.from_numpy(data[i:i + block_size].astype(np.int64)) for i in ix])
    y = torch.stack([torch.from_numpy(data[i + 1:i + 1 + block_size].astype(np.int64)) for i in ix])
    return x.to(device), y.to(device)


@torch.no_grad()
def estimate(model, train_data, val_data, args, device):
    model.eval()
    out = {}
    for name, data in [("train", train_data), ("val", val_data)]:
        losses = []
        for _ in range(args.eval_iters):
            x, y = get_batch(data, args.batch_size, args.block_size, device)
            _, loss = model(x, y)
            losses.append(loss.item())
        out[name] = sum(losses) / len(losses)
    model.train()
    return out


def save_checkpoint(path, model, optimizer, config, args, iter_num, best_val_loss):
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({
        "model": model.state_dict(),
        "optimizer": optimizer.state_dict(),
        "config": config.__dict__,
        "iter_num": iter_num,
        "best_val_loss": best_val_loss,
        "args": vars(args),
    }, path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", default="data/processed/pretrain")
    parser.add_argument("--tokenizer", default="tokenizer/newcoder.model")
    parser.add_argument("--out_dir", default="checkpoints/pretrain")
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    parser.add_argument("--block_size", type=int, default=512)
    parser.add_argument("--n_layer", type=int, default=6)
    parser.add_argument("--n_head", type=int, default=6)
    parser.add_argument("--n_embd", type=int, default=384)
    parser.add_argument("--dropout", type=float, default=0.1)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--max_iters", type=int, default=5000)
    parser.add_argument("--learning_rate", type=float, default=3e-4)
    parser.add_argument("--weight_decay", type=float, default=0.1)
    parser.add_argument("--grad_clip", type=float, default=1.0)
    parser.add_argument("--eval_interval", type=int, default=200)
    parser.add_argument("--eval_iters", type=int, default=20)
    parser.add_argument("--save_interval", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    sp = spm.SentencePieceProcessor(model_file=args.tokenizer)
    device = torch.device(args.device)
    use_amp = device.type == "cuda"

    data_dir = Path(args.data_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    train_data = np.memmap(data_dir / "train.bin", dtype=np.int32, mode="r")
    val_data = np.memmap(data_dir / "val.bin", dtype=np.int32, mode="r")

    config = GPTConfig(
        vocab_size=sp.vocab_size(),
        block_size=args.block_size,
        n_layer=args.n_layer,
        n_head=args.n_head,
        n_embd=args.n_embd,
        dropout=args.dropout,
    )
    model = GPT(config).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.learning_rate, weight_decay=args.weight_decay, betas=(0.9, 0.95))
    scaler = torch.amp.GradScaler("cuda", enabled=use_amp)

    print(f"params {sum(p.numel() for p in model.parameters()) / 1e6:.2f}M")
    print(f"train tokens {len(train_data):,}, val tokens {len(val_data):,}, device {device}")

    best_val_loss = float("inf")
    for iter_num in tqdm(range(1, args.max_iters + 1)):
        x, y = get_batch(train_data, args.batch_size, args.block_size, device)
        with torch.amp.autocast("cuda", enabled=use_amp):
            _, loss = model(x, y)
        optimizer.zero_grad(set_to_none=True)
        scaler.scale(loss).backward()
        if args.grad_clip > 0:
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), args.grad_clip)
        scaler.step(optimizer)
        scaler.update()

        if iter_num == 1 or iter_num % args.eval_interval == 0:
            losses = estimate(model, train_data, val_data, args, device)
            val_loss = losses["val"]
            print(f"\niter {iter_num}: train_loss={losses['train']:.4f}, val_loss={val_loss:.4f}, ppl={math.exp(min(val_loss, 20)):.2f}")
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                save_checkpoint(out_dir / "best.pt", model, optimizer, config, args, iter_num, best_val_loss)
                print("saved best.pt")
        if iter_num % args.save_interval == 0:
            save_checkpoint(out_dir / f"ckpt_{iter_num}.pt", model, optimizer, config, args, iter_num, best_val_loss)

    save_checkpoint(out_dir / "last.pt", model, optimizer, config, args, args.max_iters, best_val_loss)


if __name__ == "__main__":
    main()
