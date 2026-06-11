from itertools import accumulate


def running_totals(numbers: list[float]) -> list[float]:
    return list(accumulate(numbers))


def main() -> None:
    print(running_totals([1, 2, 3]))
    print(running_totals([10, -5, 8, 2]))
    print(running_totals([]))


if __name__ == "__main__":
    main()
