import string

PUNCTUATION = set(string.punctuation + "—–«»…")


def clean(text: str) -> str:
    return "".join(char for char in text if not char.isspace() and char not in PUNCTUATION)


def main() -> None:
    text = input("Введите текст: ")
    print(clean(text))


if __name__ == "__main__":
    main()
