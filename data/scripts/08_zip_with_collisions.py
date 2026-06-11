from typing import Any


def zip_merge(keys: list[Any], values: list[Any]) -> dict[Any, Any]:
    if len(keys) != len(values):
        raise ValueError("Списки ключей и значений должны быть одной длины.")
    result: dict[Any, Any] = {}
    for key, value in zip(keys, values):
        if key not in result:
            result[key] = value
        elif isinstance(result[key], list):
            result[key].append(value)
        elif isinstance(result[key], (int, float)) and isinstance(value, (int, float)):
            result[key] += value
        else:
            result[key] = [result[key], value]
    return result


def main() -> None:
    print(zip_merge(["a", "b", "a", "c"], [1, 2, 3, 4]))
    print(zip_merge(["x", "x", "x"], ["foo", "bar", "baz"]))
    print(zip_merge(["k"], [10]))


if __name__ == "__main__":
    main()
