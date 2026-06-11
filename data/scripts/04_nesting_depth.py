from typing import Any


def nesting_depth(data: Any) -> int:
    if not isinstance(data, list):
        return 0
    if not data:
        return 1
    return 1 + max(nesting_depth(item) for item in data)


def main() -> None:
    print(nesting_depth([1, 2, 3]))
    print(nesting_depth([1, [2, [3, [4]]]]))
    print(nesting_depth([]))
    print(nesting_depth(42))
    print(nesting_depth([1, [2, 3], [[4]]]))


if __name__ == "__main__":
    main()
