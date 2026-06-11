from typing import Any


def format_kwargs(**kwargs: Any) -> str:
    return ", ".join(f"{key}={value!r}" for key, value in kwargs.items())


def main() -> None:
    print(format_kwargs(name="Анна", age=30, city="Москва"))
    print(repr(format_kwargs()))


if __name__ == "__main__":
    main()
