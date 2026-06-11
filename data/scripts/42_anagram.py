def is_anagram(first: str, second: str) -> bool:
    return sorted(first) == sorted(second)


def main() -> None:
    print(is_anagram("listen", "silent"))


if __name__ == "__main__":
    main()
