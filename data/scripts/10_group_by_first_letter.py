from collections import defaultdict


def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    groups: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        if word:
            groups[word[0].lower()].append(word)
    return dict(groups)


def main() -> None:
    words = ["яблоко", "арбуз", "банан", "вишня", "Ананас", "Брусника"]
    print(group_by_first_letter(words))


if __name__ == "__main__":
    main()
