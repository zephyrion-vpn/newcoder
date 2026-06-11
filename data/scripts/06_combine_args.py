from typing import Any


def combine_args(*args: Any, **kwargs: Any) -> dict[Any, Any]:
    result: dict[Any, Any] = {index: value for index, value in enumerate(args)}
    result.update(kwargs)
    return result


def main() -> None:
    print(combine_args("a", "b", x=1, y=2))
    print(combine_args(10, 20, 30))
    print(combine_args(name="Анна"))


if __name__ == "__main__":
    main()
