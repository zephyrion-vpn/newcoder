def read_positive_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите корректное число.")
            continue
        if value <= 0:
            print("Сторона должна быть положительной.")
            continue
        return value


def main() -> None:
    width = read_positive_number("Введите ширину прямоугольника: ")
    height = read_positive_number("Введите высоту прямоугольника: ")

    area = width * height
    perimeter = 2 * (width + height)

    print(f"Площадь: {area}")
    print(f"Периметр: {perimeter}")


if __name__ == "__main__":
    main()
