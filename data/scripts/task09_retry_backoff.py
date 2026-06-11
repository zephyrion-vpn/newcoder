import functools
import time
from typing import Any, Callable, TypeVar

T = TypeVar("T")


def retry(
    attempts: int = 4,
    base_delay: float = 0.1,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            delay = base_delay
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as error:
                    if attempt == attempts:
                        raise
                    print(f"Попытка {attempt} неудачна ({error}), пауза {delay:.2f}с")
                    time.sleep(delay)
                    delay *= 2
            raise RuntimeError("Недостижимый код")
        return wrapper
    return decorator


_counter = {"value": 0}


@retry(attempts=4, base_delay=0.05)
def flaky() -> str:
    _counter["value"] += 1
    if _counter["value"] < 3:
        raise ConnectionError("временный сбой")
    return "успех"


def main() -> None:
    print("Результат:", flaky())
    print("Всего вызовов:", _counter["value"])


if __name__ == "__main__":
    main()
