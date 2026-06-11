from numbers import Number
from typing import Any


def nested_sum(data: Any) -> float:
    if isinstance(data, (list, tuple)):
        return sum(nested_sum(item) for item in data)
    if isinstance(data, bool):
        return 0
    if isinstance(data, Number):
        return data
    return 0


def main() -> None:
    print(nested_sum([1, [2, 3], [[4], 5], [[[6]]]]))
    print(nested_sum([1, "a", [2, None, [3.5]]]))
    print(nested_sum([]))


if __name__ == "__main__":
    main()
