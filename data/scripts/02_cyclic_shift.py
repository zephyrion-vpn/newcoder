from typing import Any


def is_cyclic_shift(first: list[Any], second: list[Any]) -> bool:
    if len(first) != len(second):
        return False
    if not first:
        return True
    doubled = first + first
    n = len(first)
    for start in range(n):
        if doubled[start:start + n] == second:
            return True
    return False


def main() -> None:
    print(is_cyclic_shift([3, 4, 5, 1, 2], [1, 2, 3, 4, 5]))
    print(is_cyclic_shift([1, 2, 3], [3, 1, 2]))
    print(is_cyclic_shift([1, 2, 3], [3, 2, 1]))
    print(is_cyclic_shift([1, 2], [1, 2, 3]))
    print(is_cyclic_shift([], []))


if __name__ == "__main__":
    main()
