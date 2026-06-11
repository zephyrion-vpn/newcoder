from typing import Any, Iterable, Iterator


def cycle_with_limit(iterable: Iterable[Any], limit: int) -> Iterator[Any]:
    if limit < 0:
        raise ValueError("limit должен быть неотрицательным.")
    items = list(iterable)
    if not items:
        return
    for _ in range(limit):
        for item in items:
            yield item


def main() -> None:
    print(list(cycle_with_limit([1, 2, 3], 2)))
    print(list(cycle_with_limit("ab", 3)))
    print(list(cycle_with_limit([1, 2], 0)))


if __name__ == "__main__":
    main()
