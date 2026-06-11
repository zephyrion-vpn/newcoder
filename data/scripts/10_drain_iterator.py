from typing import Any, Iterator


def drain(iterator: Iterator[Any]) -> list[Any]:
    return list(iterator)


def main() -> None:
    source = iter([1, 2, 3, 4])
    drained = drain(source)
    print(f"Извлечено: {drained}")
    print(f"Остаток источника: {list(source)}")


if __name__ == "__main__":
    main()
