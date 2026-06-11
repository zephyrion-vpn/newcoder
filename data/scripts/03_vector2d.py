from __future__ import annotations

import math


class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector2D) and (self.x, self.y) == (other.x, other.y)

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"


def main() -> None:
    a = Vector2D(3, 4)
    b = Vector2D(1, 2)
    print(a + b)
    print(a - b)
    print(abs(a))


if __name__ == "__main__":
    main()
