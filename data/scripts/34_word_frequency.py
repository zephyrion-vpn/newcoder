from collections import Counter


def word_frequency(text: str) -> dict[str, int]:
    return dict(Counter(text.lower().split()))


def main() -> None:
    text = input("Введите текст: ")
    for word, count in word_frequency(text).items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
