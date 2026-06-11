import re


def remove_numeric_words(text: str) -> str:
    without = re.sub(r"\b\d+\b", "", text)
    return re.sub(r"\s+", " ", without).strip()


def main() -> None:
    print(remove_numeric_words("У меня 2 кошки и 15 рыбок, а также abc123 текст."))


if __name__ == "__main__":
    main()
