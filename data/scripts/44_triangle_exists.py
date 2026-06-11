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


def triangle_exists(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a


def main() -> None:
    a = read_positive_number("Введите сторону a: ")
    b = read_positive_number("Введите сторону b: ")
    c = read_positive_number("Введите сторону c: ")
    print("Треугольник существует." if triangle_exists(a, b, c) else "Треугольник не существует.")


if __name__ == "__main__":
    main()
