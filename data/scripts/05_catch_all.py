import functools
import logging
from typing import Any, Callable, TypeVar

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

T = TypeVar("T")


def safe(default: T) -> Callable[[Callable[..., T]], Callable[..., T]]:
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


@safe(default=-1)
def divide(a: int, b: int) -> int:
    return a // b


def main() -> None:
    print(divide(10, 2))
    print(divide(10, 0))


if __name__ == "__main__":
    main()
