from typing import Any, Callable


def my_map(func: Callable[[Any], Any], items: list[Any]) -> list[Any]:
    return [func(item) for item in items]


def main() -> None:
    print(my_map(lambda x: x ** 2, [1, 2, 3, 4]))
    print(my_map(str.upper, ["a", "b", "c"]))
    print(my_map(len, ["hello", "hi", "hey"]))


if __name__ == "__main__":
    main()
