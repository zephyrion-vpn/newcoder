from typing import Any


def is_subset(small: dict[Any, Any], big: dict[Any, Any]) -> bool:
    return all(key in big and big[key] == value for key, value in small.items())


def main() -> None:
    big = {"a": 1, "b": 2, "c": 3}
    print(is_subset({"a": 1, "b": 2}, big))
    print(is_subset({"a": 1, "x": 9}, big))
    print(is_subset({"a": 99}, big))
    print(is_subset({}, big))


if __name__ == "__main__":
    main()
