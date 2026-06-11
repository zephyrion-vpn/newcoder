import functools
from typing import Callable, TypeVar

T = TypeVar("T")


def singleton(cls: type[T]) -> Callable[..., T]:
    instances: dict[type, T] = {}

    @functools.wraps(cls, updated=())
    def get_instance(*args: object, **kwargs: object) -> T:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Config:
    def __init__(self, name: str = "default") -> None:
        self.name = name


def main() -> None:
    a = Config("first")
    b = Config("second")
    print(f"a.name = {a.name!r}, b.name = {b.name!r}")
    print(f"a и b — один объект: {a is b}")
    print(f"Имя сохранило обёрнутый класс: {Config.__name__}")


if __name__ == "__main__":
    main()
