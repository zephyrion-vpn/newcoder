from typing import Any


def filter_long_strings(data: dict[Any, Any], min_length: int = 3) -> dict[Any, str]:
    return {
        key: value
        for key, value in data.items()
        if isinstance(value, str) and len(value) > min_length
    }


def main() -> None:
    data = {"a": "ok", "b": "hello", "c": 123, "d": "world", "e": "hi"}
    print(filter_long_strings(data))
    print(filter_long_strings({}))


if __name__ == "__main__":
    main()
