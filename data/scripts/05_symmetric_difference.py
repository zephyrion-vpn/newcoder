from typing import Any


def symmetric_difference(a: set[Any], b: set[Any]) -> set[Any]:
    only_a = a - b
    only_b = b - a
    return only_a | only_b


def main() -> None:
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(sorted(symmetric_difference(a, b)))
    print(sorted(symmetric_difference({1, 2}, set())))
    print(sorted(symmetric_difference({1, 2}, {1, 2})))


if __name__ == "__main__":
    main()
