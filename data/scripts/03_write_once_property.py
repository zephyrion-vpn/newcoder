class WriteOnce:
    def __init__(self, name: str) -> None:
        self.private_name = f"_{name}"

    def __set_name__(self, owner: type, name: str) -> None:
        self.private_name = f"_{name}"

    def __get__(self, instance: object, owner: type | None = None) -> object:
        if instance is None:
            return self
        if not hasattr(instance, self.private_name):
            raise AttributeError("Значение ещё не установлено.")
        return getattr(instance, self.private_name)

    def __set__(self, instance: object, value: object) -> None:
        if hasattr(instance, self.private_name):
            raise AttributeError("Атрибут неизменяем после установки.")
        setattr(instance, self.private_name, value)


class Point:
    x = WriteOnce("x")
    y = WriteOnce("y")

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


def main() -> None:
    p = Point(3, 4)
    print(f"p.x = {p.x}, p.y = {p.y}")
    try:
        p.x = 99
    except AttributeError as error:
        print(f"Попытка изменить p.x → {error}")
    print(f"p.x после попытки: {p.x}")


if __name__ == "__main__":
    main()
