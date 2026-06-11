from functools import wraps
from typing import Any, Callable


def retry(max_attempts: int = 3) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    if max_attempts < 1:
        raise ValueError("max_attempts должно быть не меньше 1.")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error: Exception | None = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    last_error = error
                    print(f"Попытка {attempt} не удалась: {error}")
            raise last_error
        return wrapper
    return decorator


_calls = {"count": 0}


@retry(max_attempts=3)
def flaky() -> str:
    _calls["count"] += 1
    if _calls["count"] < 3:
        raise ValueError("временный сбой")
    return "успех"


def main() -> None:
    print(flaky())


if __name__ == "__main__":
    main()
