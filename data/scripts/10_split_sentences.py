import re

SENTENCE_PATTERN = re.compile(r"[^.!?]+[.!?]*")


def split_sentences(text: str) -> list[str]:
    return [sentence.strip() for sentence in SENTENCE_PATTERN.findall(text) if sentence.strip()]


def main() -> None:
    text = "Привет! Как дела? Всё хорошо. Это тест."
    for sentence in split_sentences(text):
        print(sentence)


if __name__ == "__main__":
    main()
