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
        print(result)
    print("После подавленного деления на ноль.")

    with suppress_error(KeyError, IndexError):
        _ = {}["missing"]
    print("После подавленного KeyError.")

    try:
        with suppress_error(ValueError):
            raise TypeError("не подавляется")
    except TypeError as error:
        print(f"Проброшено: {error}")


if __name__ == "__main__":
    main()
