import argparse
from pathlib import Path
import sentencepiece as spm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/processed/tokenizer_corpus.txt")
    parser.add_argument("--model_prefix", default="tokenizer/newcoder")
    parser.add_argument("--vocab_size", type=int, default=2000)
    args = parser.parse_args()
    Path(args.model_prefix).parent.mkdir(parents=True, exist_ok=True)
    spm.SentencePieceTrainer.Train(
        input=args.input,
        model_prefix=args.model_prefix,
        vocab_size=args.vocab_size,
        model_type="bpe",
        character_coverage=1.0,
        bos_id=1,
        eos_id=2,
        pad_id=0,
        unk_id=3,
        user_defined_symbols=["<|system|>", "<|user|>", "<|assistant|>", "<|end|>", "<|file|>", "<|text|>"],
        input_sentence_size=1000000,
        shuffle_input_sentence=True,
    )
    print("saved", args.model_prefix + ".model")


if __name__ == "__main__":
    main()
