from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    category: str
    in_stock: bool


class Specification(ABC):
    @abstractmethod
    def is_satisfied_by(self, item: object) -> bool: ...

    def __and__(self, other: "Specification") -> "Specification":
        return AndSpecification(self, other)

    def __or__(self, other: "Specification") -> "Specification":
        return OrSpecification(self, other)

    def __invert__(self) -> "Specification":
        return NotSpecification(self)


class AndSpecification(Specification):
    def __init__(self, *specs: Specification) -> None:
        self.specs = specs

    def is_satisfied_by(self, item: object) -> bool:
        return all(spec.is_satisfied_by(item) for spec in self.specs)


class OrSpecification(Specification):
    def __init__(self, *specs: Specification) -> None:
        self.specs = specs

    def is_satisfied_by(self, item: object) -> bool:
        return any(spec.is_satisfied_by(item) for spec in self.specs)


class NotSpecification(Specification):
    def __init__(self, spec: Specification) -> None:
        self.spec = spec

    def is_satisfied_by(self, item: object) -> bool:
        return not self.spec.is_satisfied_by(item)


class CheaperThan(Specification):
    def __init__(self, limit: float) -> None:
        self.limit = limit

    def is_satisfied_by(self, item: Product) -> bool:
        return item.price < self.limit


class InCategory(Specification):
    def __init__(self, category: str) -> None:
        self.category = category

    def is_satisfied_by(self, item: Product) -> bool:
        return item.category == self.category


class InStock(Specification):
    def is_satisfied_by(self, item: Product) -> bool:
        return item.in_stock


def main() -> None:
    products = [
        Product("Ноутбук", 1200, "Электроника", True),
        Product("Мышь", 25, "Электроника", True),
        Product("Книга", 15, "Книги", False),
        Product("Наушники", 80, "Электроника", False),
    ]

    cheap_electronics = InCategory("Электроника") & CheaperThan(100) & InStock()
    print("Дешёвая электроника в наличии:")
    for p in filter(cheap_electronics.is_satisfied_by, products):
        print(f"   {p.name}")

    not_in_stock = ~InStock()
    print("\nНет в наличии:")
    for p in filter(not_in_stock.is_satisfied_by, products):
        print(f"   {p.name}")

    books_or_cheap = InCategory("Книги") | CheaperThan(30)
    print("\nКниги или дешевле 30:")
    for p in filter(books_or_cheap.is_satisfied_by, products):
        print(f"   {p.name}")


if __name__ == "__main__":
    main()
