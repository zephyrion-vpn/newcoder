# newcoder_full_from_scratch

Полный пайплайн для обучения маленькой coder-модели **с нуля** на твоих Python-скриптах.

Готовые модели не используются. С нуля обучаются:

1. собственный SentencePiece/BPE tokenizer;
2. GPT-like decoder-only модель;
3. pretraining на сыром коде и простых объяснениях;
4. SFT/instruction tuning на автоматически созданном JSONL.

## Быстрый старт

```bash
pip install -r requirements.txt
python 01_build_corpus_and_sft.py --scripts_dir data/scripts --out_dir data/processed
python 02_train_tokenizer.py --input data/processed/tokenizer_corpus.txt --model_prefix tokenizer/newcoder --vocab_size 2000
python 03_prepare_pretrain.py --input data/processed/pretrain_corpus.txt --tokenizer tokenizer/newcoder.model --out_dir data/processed/pretrain --block_size 512
python 04_train_pretrain.py --data_dir data/processed/pretrain --tokenizer tokenizer/newcoder.model --out_dir checkpoints/pretrain --device cuda --n_layer 6 --n_head 6 --n_embd 384 --block_size 512 --batch_size 16 --max_iters 5000
python 05_prepare_sft.py --input data/processed/sft_dataset.jsonl --tokenizer tokenizer/newcoder.model --out_dir data/processed/sft --max_length 1024
python 06_train_sft.py --data_dir data/processed/sft --tokenizer tokenizer/newcoder.model --init_checkpoint checkpoints/pretrain/best.pt --out_dir checkpoints/sft --device cuda --n_layer 6 --n_head 6 --n_embd 384 --block_size 1024 --batch_size 8 --max_iters 3000
python 07_generate.py --checkpoint checkpoints/sft/best.pt --tokenizer tokenizer/newcoder.model --prompt_file prompt.txt --device cuda --temperature 0.2 --top_k 40 --max_new_tokens 300
```

Если GPU нет, замени `--device cuda` на `--device cpu`, а batch_size уменьши до 2-4.

## Если tokenizer ругается на vocab_size

Попробуй меньше словарь:

```bash
python 02_train_tokenizer.py --input data/processed/tokenizer_corpus.txt --model_prefix tokenizer/newcoder --vocab_size 1000
```

## Что важно

- Файлы из `data/scripts` используются для сборки pretraining corpus и SFT examples.
- `pretrain` нужен обязательно: без него модель со случайными весами плохо пишет язык.
- SFT считает loss только по ответу ассистента, prompt маскируется.
- Это всё ещё маленький корпус. Качество станет лучше прежнего byte-level/SFT-only варианта, но для сильной модели нужно больше данных.
