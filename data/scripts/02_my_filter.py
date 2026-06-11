from typing import Any, Callable


def my_filter(items: list[Any], predicate: Callable[[Any], bool]) -> list[Any]:
    return [item for item in items if predicate(item)]


def main() -> None:
    print(my_filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
    print(my_filter(["a", "", "b", "", "c"], bool))
    print(my_filter([], lambda x: True))


if __name__ == "__main__":
    main()
