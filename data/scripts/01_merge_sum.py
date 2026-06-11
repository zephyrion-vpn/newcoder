from collections import defaultdict
from typing import Any


def merge_sum(dicts: list[dict[Any, float]]) -> dict[Any, float]:
    result: defaultdict[Any, float] = defaultdict(float)
    for current in dicts:
        for key, value in current.items():
            result[key] += value
    return dict(result)


def main() -> None:
    data = [{"a": 1, "b": 2}, {"a": 3, "c": 4}, {"b": 5, "c": 6}]
    print(merge_sum(data))
    print(merge_sum([]))


if __name__ == "__main__":
    main()
