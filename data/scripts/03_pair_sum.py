def find_pairs(numbers: list[int], target: int) -> list[tuple[int, int]]:
    seen: set[int] = set()
    pairs: set[tuple[int, int]] = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            pairs.add((min(number, complement), max(number, complement)))
        seen.add(number)
    return sorted(pairs)


def main() -> None:
    numbers = [2, 4, 3, 5, 7, 8, 1, 6, 4]
    print(find_pairs(numbers, 9))
    print(find_pairs([1, 1, 2, 3], 2))
    print(find_pairs([], 5))


if __name__ == "__main__":
    main()
