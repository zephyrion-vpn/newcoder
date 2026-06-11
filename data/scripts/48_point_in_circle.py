def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите корректное число.")


def read_positive_number(prompt: str) -> float:
    while True:
        value = read_number(prompt)
        if value > 0:
            return value
        print("Радиус должен быть положительным.")


def main() -> None:
    x = read_number("Введите X: ")
    y = read_number("Введите Y: ")
    radius = read_positive_number("Введите радиус R: ")
    if x ** 2 + y ** 2 < radius ** 2:
        print("Точка внутри круга.")
    elif x ** 2 + y ** 2 == radius ** 2:
        print("Точка на границе круга.")
    else:
        print("Точка вне круга.")


if __name__ == "__main__":
    main()
