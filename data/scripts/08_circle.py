import math


def read_positive_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите корректное число.")
            continue
        if value <= 0:
            print("Радиус должен быть положительным.")
            continue
        return value


def main() -> None:
    radius = read_positive_number("Введите радиус круга: ")
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print(f"Длина окружности: {circumference}")
    print(f"Площадь круга: {area}")


if __name__ == "__main__":
    main()
