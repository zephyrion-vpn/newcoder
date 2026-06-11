from typing import Any, Callable


class SafeCalculator:
    @staticmethod
    def _safe(operation: Callable[[], Any]) -> dict[str, Any]:
        try:
            return {"success": True, "result": operation(), "error": ""}
        except Exception as error:
            return {"success": False, "result": None, "error": f"{type(error).__name__}: {error}"}

    def add(self, a: float, b: float) -> dict[str, Any]:
        return self._safe(lambda: a + b)

    def subtract(self, a: float, b: float) -> dict[str, Any]:
        return self._safe(lambda: a - b)

    def multiply(self, a: float, b: float) -> dict[str, Any]:
        return self._safe(lambda: a * b)

    def divide(self, a: float, b: float) -> dict[str, Any]:
        return self._safe(lambda: a / b)

    def power(self, a: float, b: float) -> dict[str, Any]:
        return self._safe(lambda: a ** b)

    def sqrt(self, a: float) -> dict[str, Any]:
        def op() -> float:
            if a < 0:
                raise ValueError("корень из отрицательного числа")
            return a ** 0.5
        return self._safe(op)


def main() -> None:
    calc = SafeCalculator()
    print("2 + 3 =", calc.add(2, 3))
    print("10 / 0 =", calc.divide(10, 0))
    print("sqrt(-4) =", calc.sqrt(-4))
    print("sqrt(16) =", calc.sqrt(16))
    print("2 ** 10 =", calc.power(2, 10))
    print('"a" * 3 =', calc.multiply("a", 3))


if __name__ == "__main__":
    main()
