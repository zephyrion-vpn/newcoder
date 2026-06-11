import inspect
import sys
from typing import Type


class Shape:
    def area(self) -> float:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


class NotAShape:
    pass


def find_subclasses(base: Type, module_name: str = "__main__") -> list[Type]:
    module = sys.modules[module_name]
    found = []
    for _, obj in inspect.getmembers(module, inspect.isclass):
        if issubclass(obj, base) and obj is not base:
            found.append(obj)
    return found


def main() -> None:
    subclasses = find_subclasses(Shape)
    print("Найдено подклассов Shape:")
    for cls in subclasses:
        print(f"   {cls.__name__}")
    print(f"\nNotAShape в списке: {NotAShape in subclasses} (ожидается False)")


if __name__ == "__main__":
    main()
