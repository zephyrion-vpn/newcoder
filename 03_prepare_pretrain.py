import argparse
import json
from pathlib import Path
import numpy as np
import sentencepiece as spm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/processed/pretrain_corpus.txt")
    parser.add_argument("--tokenizer", default="tokenizer/newcoder.model")
    parser.add_argument("--out_dir", default="data/processed/pretrain")
    parser.add_argument("--val_ratio", type=float, default=0.05)
    args = parser.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    sp = spm.SentencePieceProcessor(model_file=args.tokenizer)
    text = Path(args.input).read_text(encoding="utf-8")
    ids = sp.encode(text, out_type=int, add_bos=True, add_eos=True)
    arr = np.array(ids, dtype=np.int32)
    split = max(1, int(len(arr) * (1 - args.val_ratio)))
    arr[:split].tofile(out / "train.bin")
    arr[split:].tofile(out / "val.bin")
    meta = {"tokens": int(len(arr)), "train_tokens": int(split), "val_tokens": int(len(arr) - split), "vocab_size": sp.vocab_size()}
    (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
