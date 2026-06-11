import argparse
import json
import random
from pathlib import Path

import sentencepiece as spm
import torch


def build_prompt(example):
    return f"""<|system|>
Ты — маленькая coder-модель, обученная с нуля. Отвечай строго по задаче и не выдумывай поведение, которого нет в коде.
<|user|>
{example['input'].strip()}
<|assistant|>
"""


def build_answer(example):
    return example["output"].strip() + "\n<|end|>"


def encode_example(example, sp, max_length):
    prompt = build_prompt(example)
    full = prompt + build_answer(example)
    prompt_ids = sp.encode(prompt, out_type=int, add_bos=True, add_eos=False)
    ids = sp.encode(full, out_type=int, add_bos=True, add_eos=True)[:max_length]
    input_ids = ids[:-1]
    labels = ids[1:]
    prompt_len = min(len(prompt_ids), len(labels))
    for i in range(max(0, prompt_len - 1)):
        labels[i] = -1
    return {"id": example.get("id", ""), "task_type": example.get("task_type", ""), "input_ids": input_ids, "labels": labels}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/processed/sft_dataset.jsonl")
    parser.add_argument("--tokenizer", default="tokenizer/newcoder.model")
    parser.add_argument("--out_dir", default="data/processed/sft")
    parser.add_argument("--max_length", type=int, default=1024)
    parser.add_argument("--val_ratio", type=float, default=0.08)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    sp = spm.SentencePieceProcessor(model_file=args.tokenizer)
    rows = [json.loads(line) for line in Path(args.input).read_text(encoding="utf-8").splitlines() if line.strip()]
    random.seed(args.seed)
    random.shuffle(rows)
    val_size = max(1, int(len(rows) * args.val_ratio))
    val_rows = rows[:val_size]
    train_rows = rows[val_size:]
    torch.save([encode_example(e, sp, args.max_length) for e in train_rows], out_dir / "train.pt")
    torch.save([encode_example(e, sp, args.max_length) for e in val_rows], out_dir / "val.pt")
    meta = {"train_examples": len(train_rows), "val_examples": len(val_rows), "vocab_size": sp.vocab_size(), "max_length": args.max_length, "loss_masking": "prompt ignored"}
    (out_dir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
