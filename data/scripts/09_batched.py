from itertools import islice
from typing import Any, Iterable, Iterator


def batched(iterable: Iterable[Any], size: int) -> Iterator[tuple[Any, ...]]:
    if size < 1:
        raise ValueError("size должен быть не меньше 1.")
    iterator = iter(iterable)
    while True:
        chunk = tuple(islice(iterator, size))
        if not chunk:
            return
        yield chunk


def main() -> None:
    print(list(batched([1, 2, 3, 4, 5, 6, 7], 3)))
    print(list(batched("abcdef", 2)))
    print(list(batched([], 3)))


if __name__ == "__main__":
    main()
