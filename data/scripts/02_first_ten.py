from itertools import count, islice
from typing import Iterator


def naturals() -> Iterator[int]:
    yield from count(1)


def first_ten(iterator: Iterator[int]) -> list[int]:
    return list(islice(iterator, 10))


def main() -> None:
    print(first_ten(naturals()))


if __name__ == "__main__":
    main()
