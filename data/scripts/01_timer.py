import time
from functools import wraps
from typing import Any, Callable


def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            print(f"{func.__name__} выполнилась за {elapsed:.6f} сек.")
    return wrapper


@timer
def slow_sum(n: int) -> int:
    return sum(range(n))


def main() -> None:
    print(slow_sum(1_000_000))


if __name__ == "__main__":
    main()
