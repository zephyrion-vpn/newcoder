import re

WORD_WITHOUT_A = re.compile(r"\b[^\W\d_]*[^\W\d_aAаА][^\W\d_]*\b", re.UNICODE)


def words_without_a(text: str) -> list[str]:
    return [
        word
        for word in re.findall(r"\b[^\W\d_]+\b", text, re.UNICODE)
        if "a" not in word.lower() and "а" not in word.lower()
    ]


def main() -> None:
    text = "Мама мыла раму, но кот спал. Cat dog fox."
    print(words_without_a(text))


if __name__ == "__main__":
    main()
