from itertools import zip_longest
from typing import Any, Iterable, Iterator


def interleave_pairs(first: Iterable[Any], second: Iterable[Any]) -> Iterator[tuple[Any, Any]]:
    yield from zip_longest(first, second, fillvalue=None)


def main() -> None:
    a = (x for x in [1, 2, 3])
    b = (y for y in ["a", "b", "c", "d", "e"])
    print(list(interleave_pairs(a, b)))


if __name__ == "__main__":
    main()
