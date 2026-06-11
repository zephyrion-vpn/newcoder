import functools
import logging
from typing import Any, Callable, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")


def catch_exceptions(default: T) -> Callable[[Callable[..., T]], Callable[..., T]]:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            try:
                return func(*args, **kwargs)
            except Exception:
                logger.exception("Ошибка в функции %s", func.__name__)
                return default
        return wrapper
    return decorator


@catch_exceptions(default=-1)
def divide(a: int, b: int) -> int:
    return a // b


def main() -> None:
    logging.basicConfig(level=logging.ERROR, format="%(levelname)s: %(message)s")
    print("8 // 2 =", divide(8, 2))
    print("8 // 0 =", divide(8, 0))


if __name__ == "__main__":
    main()
