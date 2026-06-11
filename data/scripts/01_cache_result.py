from functools import wraps
from typing import Any, Callable


def cache_result(func: Callable[..., Any]) -> Callable[..., Any]:
    cache: dict[tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
            print(f"Вычислено {func.__name__}{args}")
        else:
            print(f"Из кэша {func.__name__}{args}")
        return cache[key]

    return wrapper


@cache_result
def slow_square(n: int) -> int:
    return n * n


def main() -> None:
    print(slow_square(4))
    print(slow_square(4))
    print(slow_square(5))


if __name__ == "__main__":
    main()
