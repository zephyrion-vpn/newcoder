from typing import Any


def union_all(sets: list[set[Any]]) -> set[Any]:
    result: set[Any] = set()
    for current in sets:
        result |= current
    return result


def main() -> None:
    print(sorted(union_all([{1, 2}, {2, 3}, {3, 4, 5}])))
    print(union_all([]))
    print(sorted(union_all([{1}, set(), {2}])))


if __name__ == "__main__":
    main()
