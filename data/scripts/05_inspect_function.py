import inspect
from typing import Callable


def describe(func: Callable) -> dict[str, object]:
    signature = inspect.signature(func)
    try:
        source = inspect.getsource(func)
    except (OSError, TypeError):
        source = "<исходный код недоступен>"
    return {
        "name": func.__name__,
        "signature": str(signature),
        "annotations": dict(inspect.get_annotations(func)),
        "doc": inspect.getdoc(func),
        "source": source,
    }


def sample(a: int, b: str = "x", *args: float, **kwargs: bool) -> list[str]:
    """Пример функции для интроспекции."""
    return [str(a), b]


def main() -> None:
    info = describe(sample)
    print("Имя:", info["name"])
    print("Сигнатура:", info["signature"])
    print("Аннотации:", info["annotations"])
    print("Docstring:", info["doc"])
    print("Исходный код:")
    print(info["source"])


if __name__ == "__main__":
    main()
