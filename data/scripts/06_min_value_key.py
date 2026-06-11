from typing import Any


def min_value_key(data: dict[Any, float]) -> Any:
    candidates = {key: value for key, value in data.items() if value}
    if not candidates:
        return None
    return min(candidates, key=candidates.get)


def main() -> None:
    data = {"a": 5, "b": 0, "c": 2, "d": None, "e": 8}
    print(min_value_key(data))
    print(min_value_key({"x": 0, "y": None}))
    print(min_value_key({}))


if __name__ == "__main__":
    main()
