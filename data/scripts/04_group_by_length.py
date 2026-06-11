from collections import defaultdict


def group_by_length(strings: list[str]) -> dict[int, list[str]]:
    groups: defaultdict[int, list[str]] = defaultdict(list)
    for text in strings:
        groups[len(text)].append(text)
    return dict(groups)


def main() -> None:
    words = ["a", "bb", "cc", "ddd", "e", "ffff"]
    print(group_by_length(words))
    print(group_by_length([]))


if __name__ == "__main__":
    main()
