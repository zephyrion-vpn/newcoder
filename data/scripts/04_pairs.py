from itertools import combinations
from typing import Any


def all_pairs(items: list[Any]) -> list[tuple[Any, Any]]:
    return list(combinations(items, 2))


def main() -> None:
    print(all_pairs([1, 2, 3, 4]))
    print(all_pairs(["a", "b", "c"]))
    print(all_pairs([1]))


if __name__ == "__main__":
    main()
