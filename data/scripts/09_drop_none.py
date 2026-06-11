from typing import Any


def drop_none(data: Any) -> Any:
    if isinstance(data, dict):
        return {
            key: drop_none(value)
            for key, value in data.items()
            if value is not None
        }
    if isinstance(data, list):
        return [drop_none(item) for item in data]
    return data


def main() -> None:
    data = {
        "a": 1,
        "b": None,
        "c": {"d": None, "e": 2, "f": {"g": None, "h": 3}},
        "i": [{"j": None, "k": 4}],
    }
    print(drop_none(data))


if __name__ == "__main__":
    main()
