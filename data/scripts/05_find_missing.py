def find_missing(numbers: list[int]) -> int:
    n = len(numbers) + 1
    expected = n * (n + 1) // 2
    return expected - sum(numbers)


def main() -> None:
    print(find_missing([1, 2, 4, 5]))
    print(find_missing([2, 3, 4]))
    print(find_missing([1, 2, 3]))


if __name__ == "__main__":
    main()
