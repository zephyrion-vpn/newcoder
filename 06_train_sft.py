import argparse
import math
import random
from pathlib import Path

import sentencepiece as spm
import torch
from torch.nn.utils.rnn import pad_sequence
from tqdm import tqdm

from model import GPT, GPTConfig


def load_examples(path):
    return torch.load(path, weights_only=False)


def collate(batch, pad_id, device):
    x = pad_sequence([torch.tensor(e["input_ids"], dtype=torch.long) for e in batch], batch_first=True, padding_value=pad_id)
    y = pad_sequence([torch.tensor(e["labels"], dtype=torch.long) for e in batch], batch_first=True, padding_value=-1)
    return x.to(device), y.to(device)


def get_batch(examples, batch_size, pad_id, device):
    return collate(random.sample(examples, min(batch_size, len(examples))), pad_id, device)


@torch.no_grad()
def estimate(model, examples, args, pad_id, device):
    model.eval()
    losses = []
    for _ in range(args.eval_iters):
        x, y = get_batch(examples, args.batch_size, pad_id, device)
        _, loss = model(x, y)
        losses.append(loss.item())
    model.train()
    return sum(losses) / len(losses)


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
    parser.add_argument("--data_dir", default="data/processed/sft")
    parser.add_argument("--tokenizer", default="tokenizer/newcoder.model")
    parser.add_argument("--init_checkpoint", default="checkpoints/pretrain/best.pt")
    parser.add_argument("--out_dir", default="checkpoints/sft")
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    parser.add_argument("--block_size", type=int, default=512)
    parser.add_argument("--n_layer", type=int, default=6)
    parser.add_argument("--n_head", type=int, default=6)
    parser.add_argument("--n_embd", type=int, default=384)
    parser.add_argument("--dropout", type=float, default=0.1)
    parser.add_argument("--batch_size", type=int, default=8)
    parser.add_argument("--max_iters", type=int, default=3000)
    parser.add_argument("--learning_rate", type=float, default=2e-4)
    parser.add_argument("--weight_decay", type=float, default=0.05)
    parser.add_argument("--grad_clip", type=float, default=1.0)
    parser.add_argument("--eval_interval", type=int, default=100)
    parser.add_argument("--eval_iters", type=int, default=20)
    parser.add_argument("--save_interval", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    random.seed(args.seed)
    torch.manual_seed(args.seed)

    sp = spm.SentencePieceProcessor(model_file=args.tokenizer)
    pad_id = sp.pad_id()
    if pad_id < 0:
        pad_id = 0

    device = torch.device(args.device)
    use_amp = device.type == "cuda"

    train_examples = load_examples(Path(args.data_dir) / "train.pt")
    val_examples = load_examples(Path(args.data_dir) / "val.pt")

    config = GPTConfig(
        vocab_size=sp.vocab_size(),
        block_size=args.block_size,
        n_layer=args.n_layer,
        n_head=args.n_head,
        n_embd=args.n_embd,
        dropout=args.dropout,
    )
    model = GPT(config).to(device)

    ckpt_path = Path(args.init_checkpoint)
    if ckpt_path.exists():
        ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
        try:
            model.load_state_dict(ckpt["model"], strict=True)
            print(f"loaded init checkpoint: {ckpt_path}")
        except Exception as e:
            print(f"warning: strict load failed: {e}")
            print("Trying non-strict load. Make sure block_size and architecture match pretraining.")
            model.load_state_dict(ckpt["model"], strict=False)
    else:
        print("warning: init checkpoint not found, training SFT from random weights")

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.learning_rate, weight_decay=args.weight_decay, betas=(0.9, 0.95))
    scaler = torch.amp.GradScaler("cuda", enabled=use_amp)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"params {sum(p.numel() for p in model.parameters()) / 1e6:.2f}M")
    print(f"train examples {len(train_examples)}, val examples {len(val_examples)}, device {device}")
    print("SFT mode: prompt tokens are masked; loss is on assistant output only")

    best_val_loss = float("inf")
    for iter_num in tqdm(range(1, args.max_iters + 1)):
        x, y = get_batch(train_examples, args.batch_size, pad_id, device)
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
            train_loss = estimate(model, train_examples, args, pad_id, device)
            val_loss = estimate(model, val_examples, args, pad_id, device)
            print(f"\niter {iter_num}: train_loss={train_loss:.4f}, val_loss={val_loss:.4f}, ppl={math.exp(min(val_loss, 20)):.2f}")
            if val_loss < best_val_loss:
                best_val_loss = val_loss
                save_checkpoint(out_dir / "best.pt", model, optimizer, config, args, iter_num, best_val_loss)
                print("saved best.pt")
        if iter_num % args.save_interval == 0:
            save_checkpoint(out_dir / f"ckpt_{iter_num}.pt", model, optimizer, config, args, iter_num, best_val_loss)

    save_checkpoint(out_dir / "last.pt", model, optimizer, config, args, args.max_iters, best_val_loss)


if __name__ == "__main__":
    main()
