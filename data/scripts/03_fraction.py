from __future__ import annotations

import math


class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть нулём.")
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        divisor = math.gcd(abs(numerator), denominator)
        self.numerator = numerator // divisor
        self.denominator = denominator // divisor

    def __add__(self, other: "Fraction") -> "Fraction":
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def __mul__(self, other: "Fraction") -> "Fraction":
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __str__(self) -> str:
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"


def main() -> None:
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    print(f"{a} + {b} = {a + b}")
    print(f"{a} * {b} = {a * b}")
    print(f"2/4 сокращается до {Fraction(2, 4)}")


if __name__ == "__main__":
    main()
