import re

SPLIT_PATTERN = re.compile(r"[,;\s]+")


def split_text(text: str) -> list[str]:
    return [token for token in SPLIT_PATTERN.split(text.strip()) if token]


def main() -> None:
    text = "яблоко, банан;вишня   груша\nслива,,персик"
    print(split_text(text))


if __name__ == "__main__":
    main()
