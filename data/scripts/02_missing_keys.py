from typing import Any


def keys_only_in_first(first: dict[Any, Any], second: dict[Any, Any]) -> list[Any]:
    return [key for key in first if key not in second]


def main() -> None:
    a = {"x": 1, "y": 2, "z": 3}
    b = {"y": 20, "w": 40}
    print(keys_only_in_first(a, b))
    print(keys_only_in_first({}, b))


if __name__ == "__main__":
    main()
