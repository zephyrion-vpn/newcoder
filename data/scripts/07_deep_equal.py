from typing import Any


def deep_equal(a: Any, b: Any) -> bool:
    if isinstance(a, dict) and isinstance(b, dict):
        if a.keys() != b.keys():
            return False
        return all(deep_equal(a[key], b[key]) for key in a)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(deep_equal(x, y) for x, y in zip(a, b))
    return type(a) == type(b) and a == b


def main() -> None:
    first = {"a": 1, "b": {"c": [1, 2, {"d": 3}]}}
    second = {"a": 1, "b": {"c": [1, 2, {"d": 3}]}}
    third = {"a": 1, "b": {"c": [1, 2, {"d": 4}]}}
    print(deep_equal(first, second))
    print(deep_equal(first, third))
    print(deep_equal({"x": 1}, {"x": True}))


if __name__ == "__main__":
    main()
