def sort_by_unique_chars(strings: list[str]) -> list[str]:
    return sorted(strings, key=lambda s: len(set(s)))


def main() -> None:
    words = ["aaa", "abc", "ab", "abcd", "aabb"]
    print(sort_by_unique_chars(words))


if __name__ == "__main__":
    main()
