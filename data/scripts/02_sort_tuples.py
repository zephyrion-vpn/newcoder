def sort_pairs(pairs: list[tuple[int, str]]) -> list[tuple[int, str]]:
    return sorted(pairs, key=lambda pair: (pair[1], pair[0]))


def main() -> None:
    data = [(1, "b"), (3, "a"), (2, "c"), (1, "a")]
    print(sort_pairs(data))


if __name__ == "__main__":
    main()
