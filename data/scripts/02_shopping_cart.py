from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float
    quantity: int


class ShoppingCart:
    def __init__(self) -> None:
        self.items: list[Item] = []

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        if price < 0 or quantity < 1:
            raise ValueError("Цена должна быть неотрицательной, количество — положительным.")
        self.items.append(Item(name, price, quantity))

    def total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)

    def total_with_discount(self, percent: float) -> float:
        if not 0 <= percent <= 100:
            raise ValueError("Скидка должна быть в диапазоне 0–100.")
        return self.total() * (1 - percent / 100)


def main() -> None:
    cart = ShoppingCart()
    cart.add_item("Яблоко", 50, 3)
    cart.add_item("Хлеб", 40, 2)
    print(f"Итого: {cart.total()}")
    print(f"Со скидкой 10%: {cart.total_with_discount(10)}")


if __name__ == "__main__":
    main()
