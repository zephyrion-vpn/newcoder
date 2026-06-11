import functools
import time
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def retry(attempts: int = 3, base_delay: float = 0.1, factor: float = 2.0) -> Callable[[Callable[..., T]], Callable[..., T]]:
    if attempts < 1:
        raise ValueError("attempts должно быть не меньше 1.")

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            delay = base_delay
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    if attempt == attempts:
                        raise
                    print(f"Попытка {attempt} неудачна ({error}); повтор через {delay:.2f}с")
                    time.sleep(delay)
                    delay *= factor
            raise AssertionError("Недостижимый код")
        return wrapper
    return decorator


def main() -> None:
    state = {"calls": 0}

    @retry(attempts=4, base_delay=0.01)
    def flaky() -> str:
        state["calls"] += 1
        if state["calls"] < 3:
            raise ValueError("временная ошибка")
        return "успех"

    print(flaky())
    print(f"Всего вызовов: {state['calls']}")


if __name__ == "__main__":
    main()
