from typing import Any


class TypedAttribute:
    def __init__(self, expected_type: type, default: Any = None) -> None:
        self._expected_type = expected_type
        self._default = default
        self._name = ""

    def __set_name__(self, owner: type, name: str) -> None:
        self._name = f"_{name}"

    def __get__(self, instance: object, owner: type | None = None) -> Any:
        if instance is None:
            return self
        return getattr(instance, self._name, self._default)

    def __set__(self, instance: object, value: Any) -> None:
        if not isinstance(value, self._expected_type):
            raise TypeError(
                f"{self._name[1:]!r} ожидает {self._expected_type.__name__}, "
                f"получено {type(value).__name__}"
            )
        setattr(instance, self._name, value)


class Product:
    name = TypedAttribute(str)
    price = TypedAttribute(float)
    quantity = TypedAttribute(int, default=0)

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity


def main() -> None:
    item = Product("клавиатура", 49.99, 3)
    print(f"{item.name}: {item.price} x {item.quantity}")
    try:
        item.price = "дорого"
    except TypeError as error:
        print("Ошибка типа:", error)


if __name__ == "__main__":
    main()
