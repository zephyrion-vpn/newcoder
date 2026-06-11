from typing import Any, Callable


class SafeCalculator:
    def _safe(self, func: Callable[[], Any]) -> dict[str, Any]:
        try:
            return {"success": True, "result": func(), "error": ""}
        except Exception as error:
            return {"success": False, "result": None, "error": str(error)}

    def add(self, a: float, b: float) -> dict[str, Any]:
        return self._safe(lambda: a + b)

    def divide(self, a: float, b: float) -> dict[str, Any]:
        return self._safe(lambda: a / b)

    def sqrt(self, x: float) -> dict[str, Any]:
        return self._safe(lambda: x ** 0.5 if x >= 0 else _raise(ValueError("Отрицательное число")))


def _raise(error: Exception) -> Any:
    raise error


def main() -> None:
    calc = SafeCalculator()
    print(calc.add(2, 3))
    print(calc.divide(10, 0))
    print(calc.sqrt(-1))


if __name__ == "__main__":
    main()
