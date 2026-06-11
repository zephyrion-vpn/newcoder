import argparse
from pathlib import Path

import sentencepiece as spm
import torch

from model import GPT, GPTConfig


def build_prompt(user_prompt):
    return f"""<|system|>
Ты — маленькая coder-модель, обученная с нуля. Отвечай строго по задаче и не выдумывай поведение, которого нет в коде.
<|user|>
{user_prompt}
<|assistant|>
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", default="checkpoints/sft/best.pt")
    parser.add_argument("--tokenizer", default="tokenizer/newcoder.model")
    parser.add_argument("--prompt", default=None)
    parser.add_argument("--prompt_file", default=None)
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    parser.add_argument("--max_new_tokens", type=int, default=300)
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--top_k", type=int, default=40)
    args = parser.parse_args()

    if args.prompt_file:
        user_prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    elif args.prompt:
        user_prompt = args.prompt
    else:
        raise ValueError("Use --prompt or --prompt_file")

    device = torch.device(args.device)
    sp = spm.SentencePieceProcessor(model_file=args.tokenizer)
    ckpt = torch.load(args.checkpoint, map_location=device, weights_only=False)
    config = GPTConfig(**ckpt["config"])
    model = GPT(config).to(device)
    model.load_state_dict(ckpt["model"])
    model.eval()

    ids = sp.encode(build_prompt(user_prompt), out_type=int, add_bos=True, add_eos=False)
    idx = torch.tensor([ids], dtype=torch.long, device=device)

    with torch.no_grad():
        for _ in range(args.max_new_tokens):
            idx_cond = idx[:, -config.block_size:]
            logits, _ = model(idx_cond)
            logits = logits[:, -1, :] / max(args.temperature, 1e-6)
            if args.top_k and args.top_k > 0:
                values, _ = torch.topk(logits, min(args.top_k, logits.size(-1)))
                logits[logits < values[:, [-1]]] = -float("inf")
            probs = torch.softmax(logits, dim=-1)
            next_id = torch.multinomial(probs, num_samples=1)
            idx = torch.cat([idx, next_id], dim=1)
            text_so_far = sp.decode(idx[0].tolist())
            if "<|end|>" in text_so_far or int(next_id.item()) == sp.eos_id():
                break

    text = sp.decode(idx[0].tolist())
    if "<|assistant|>" in text:
        text = text.split("<|assistant|>", 1)[1]
    if "<|end|>" in text:
        text = text.split("<|end|>", 1)[0]
    print(text.strip())


if __name__ == "__main__":
    main()
