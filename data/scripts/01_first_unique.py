from collections import Counter


def first_unique(text: str) -> str | None:
    counts = Counter(text)
    for char in text:
        if counts[char] == 1:
            return char
    return None


def main() -> None:
    print(first_unique("swiss"))
    print(first_unique("миссисипи"))
    print(first_unique("aabbcc"))
    print(first_unique(""))


if __name__ == "__main__":
    main()
