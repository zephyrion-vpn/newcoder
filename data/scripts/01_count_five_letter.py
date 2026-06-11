import re

WORD_PATTERN = re.compile(r"\w+", re.UNICODE)


def count_five_letter_words(text: str) -> int:
    return sum(1 for match in WORD_PATTERN.finditer(text) if len(match.group()) == 5)


def main() -> None:
    text = "Мама мыла раму, а папа читал книгу и газет."
    print(count_five_letter_words(text))


if __name__ == "__main__":
    main()
