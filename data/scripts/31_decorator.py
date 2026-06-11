import functools
from typing import Callable


def log(func: Callable[..., object]) -> Callable[..., object]:
    @functools.wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        print("Вызов функции")
        return func(*args, **kwargs)

    return wrapper


def greet() -> None:
    print("Hello")


if __name__ == "__main__":
    logged = log(greet)
    logged()
