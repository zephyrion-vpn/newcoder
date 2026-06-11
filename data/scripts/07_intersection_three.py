from typing import Any


def intersect_three(a: list[Any], b: list[Any], c: list[Any]) -> list[Any]:
    set_b = set(b)
    set_c = set(c)
    seen: set[Any] = set()
    result: list[Any] = []
    for item in a:
        if item in set_b and item in set_c and item not in seen:
            seen.add(item)
            result.append(item)
    return result


def main() -> None:
    print(intersect_three([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 6]))
    print(intersect_three([1, 2, 2, 3], [2, 3], [2, 3, 3]))
    print(intersect_three([1], [2], [3]))


if __name__ == "__main__":
    main()
