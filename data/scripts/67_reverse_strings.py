def reverse_strings(strings: list[str]) -> list[str]:
    return [text[::-1] for text in strings]


def main() -> None:
    words = ["Python", "код", "hello"]
    print(reverse_strings(words))


if __name__ == "__main__":
    main()
