def sort_by_length(strings: list[str]) -> list[str]:
    return sorted(strings, key=len)


def main() -> None:
    words = ["banana", "a", "kiwi", "strawberry", "fig"]
    print(sort_by_length(words))


if __name__ == "__main__":
    main()
