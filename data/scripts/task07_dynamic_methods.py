from types import MethodType
from typing import Callable


class DynamicService:
    def __init__(self, methods: dict[str, Callable[..., object]]) -> None:
        for name, function in methods.items():
            if not name.isidentifier():
                raise ValueError(f"Недопустимое имя метода: {name!r}")
            setattr(self, name, MethodType(function, self))
        self.registered = tuple(methods)


def main() -> None:
    config: dict[str, Callable[..., object]] = {
        "greet": lambda self, who: f"Привет, {who}!",
        "add": lambda self, a, b: a + b,
        "describe": lambda self: f"Методы: {', '.join(self.registered)}",
    }
    service = DynamicService(config)
    print(service.greet("мир"))
    print("2 + 3 =", service.add(2, 3))
    print(service.describe())


if __name__ == "__main__":
    main()
