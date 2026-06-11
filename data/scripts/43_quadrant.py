def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите корректное число.")


def quadrant(x: float, y: float) -> str:
    if x == 0 or y == 0:
        return "Точка лежит на оси."
    if x > 0:
        return "I" if y > 0 else "IV"
    return "II" if y > 0 else "III"


def main() -> None:
    x = read_number("Введите X: ")
    y = read_number("Введите Y: ")
    result = quadrant(x, y)
    print(result if "оси" in result else f"Четверть: {result}")


if __name__ == "__main__":
    main()
