from collections import Counter


def most_and_least_common(words: list[str]) -> tuple[str, str]:
    if not words:
        raise ValueError("Список слов пуст.")
    counts = Counter(words)
    most = counts.most_common()
    return most[0][0], most[-1][0]


def main() -> None:
    words = ["яблоко", "банан", "яблоко", "вишня", "яблоко", "банан"]
    most, least = most_and_least_common(words)
    print(f"Чаще всего: {most}")
    print(f"Реже всего: {least}")


if __name__ == "__main__":
    main()
