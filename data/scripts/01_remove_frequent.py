from collections import Counter
from typing import Any


def remove_frequent(items: list[Any], max_count: int = 2) -> list[Any]:
    counts = Counter(items)
    return [item for item in items if counts[item] <= max_count]


def main() -> None:
    print(remove_frequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))
    print(remove_frequent(["a", "b", "a", "a", "c"]))
    print(remove_frequent([]))


if __name__ == "__main__":
    main()
