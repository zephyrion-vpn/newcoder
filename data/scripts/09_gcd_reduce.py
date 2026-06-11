from functools import reduce
from math import gcd


def gcd_of_list(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError("Список не должен быть пустым.")
    return reduce(gcd, numbers)


def main() -> None:
    print(gcd_of_list([12, 18, 24]))
    print(gcd_of_list([17, 5]))
    print(gcd_of_list([100]))
    print(gcd_of_list([0, 8]))


if __name__ == "__main__":
    main()
