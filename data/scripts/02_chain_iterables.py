from itertools import chain
from typing import Any


def combine(*iterables: Any) -> list[Any]:
    return list(chain(*iterables))


def main() -> None:
    numbers = [1, 2, 3]
    pair = (4, 5)
    unique = {6, 7}
    print(combine(numbers, pair, unique))


if __name__ == "__main__":
    main()
