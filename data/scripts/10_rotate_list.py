from typing import Any


def rotate_list(lst: list[Any], k: int) -> list[Any]:
    if not lst:
        return []
    k %= len(lst)
    return lst[-k:] + lst[:-k] if k else lst[:]


def main() -> None:
    print(rotate_list([1, 2, 3, 4, 5], 2))
    print(rotate_list([1, 2, 3, 4, 5], 7))
    print(rotate_list([1, 2, 3, 4, 5], 0))
    print(rotate_list([1, 2, 3, 4, 5], -1))
    print(rotate_list([], 3))


if __name__ == "__main__":
    main()
