from contextlib import contextmanager
from typing import Iterator


@contextmanager
def suppress_error(*error_types: type[BaseException]) -> Iterator[None]:
    try:
        yield
    except error_types:
        pass


def main() -> None:
    with suppress_error(ZeroDivisionError):
        result = 1 / 0
        print("эта строка не выполнится")
    print("ZeroDivisionError подавлен, продолжаем.")

    with suppress_error(KeyError, IndexError):
        _ = {"a": 1}["b"]
    print("KeyError подавлен.")

    try:
        with suppress_error(ValueError):
            raise TypeError("другой тип")
    except TypeError:
        print("TypeError НЕ подавлен (как и ожидалось) — подавляется только указанный тип.")


if __name__ == "__main__":
    main()
