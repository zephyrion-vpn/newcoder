REPLACEMENTS = {"о": "😮", "О": "😮", "а": "😺", "А": "😺"}


def replace(text: str) -> str:
    return "".join(REPLACEMENTS.get(char, char) for char in text)


def main() -> None:
    text = input("Введите текст: ")
    print(replace(text))


if __name__ == "__main__":
    main()
