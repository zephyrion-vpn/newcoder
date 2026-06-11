from operator import add, mul, sub, truediv

OPERATIONS = {"+": add, "-": sub, "*": mul, "/": truediv}


def calculate(a: float, b: float, operator: str) -> float:
    if operator not in OPERATIONS:
        raise ValueError(f"Неизвестный оператор: {operator!r}")
    if operator == "/" and b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return OPERATIONS[operator](a, b)


def main() -> None:
    print(calculate(6, 3, "+"))
    print(calculate(6, 3, "-"))
    print(calculate(6, 3, "*"))
    print(calculate(6, 3, "/"))


if __name__ == "__main__":
    main()
