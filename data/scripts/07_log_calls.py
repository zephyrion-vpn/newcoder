from functools import wraps
from typing import Any, Callable


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        parts = [repr(arg) for arg in args]
        parts += [f"{key}={value!r}" for key, value in kwargs.items()]
        print(f"Вызов {func.__name__}({', '.join(parts)})")
        return func(*args, **kwargs)
    return wrapper


@log_calls
def greet(name: str, greeting: str = "Привет") -> str:
    return f"{greeting}, {name}!"


def main() -> None:
    print(greet("Анна"))
    print(greet("Борис", greeting="Здравствуй"))


if __name__ == "__main__":
    main()
