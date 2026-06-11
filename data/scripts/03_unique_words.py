import re

WORD_PATTERN = re.compile(r"[\w]+", re.UNICODE)


def unique_words(text: str) -> set[str]:
    return {match.group().lower() for match in WORD_PATTERN.finditer(text)}


def main() -> None:
    text = "Привет, мир! Мир прекрасен; привет всем."
    print(sorted(unique_words(text)))
    print(sorted(unique_words("Hello, hello! World... world?")))


if __name__ == "__main__":
    main()
