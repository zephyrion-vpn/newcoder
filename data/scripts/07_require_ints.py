from functools import wraps
from typing import Any, Callable


def require_ints(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        for value in (*args, *kwargs.values()):
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError(f"Ожидались целые числа, получено: {value!r}")
        return func(*args, **kwargs)
    return wrapper


@require_ints
def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    print(add(2, 3))
    try:
        add(2, "3")
    except TypeError as error:
        print(f"TypeError: {error}")


if __name__ == "__main__":
    main()
