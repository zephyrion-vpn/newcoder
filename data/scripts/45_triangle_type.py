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


def triangle_type(a: float, b: float, c: float) -> str:
    distinct = len({a, b, c})
    if distinct == 1:
        return "Равносторонний"
    if distinct == 2:
        return "Равнобедренный"
    return "Разносторонний"


def main() -> None:
    a = read_positive_number("Введите сторону a: ")
    b = read_positive_number("Введите сторону b: ")
    c = read_positive_number("Введите сторону c: ")
    if not (a + b > c and a + c > b and b + c > a):
        print("Такой треугольник не существует.")
        return
    print(f"Тип треугольника: {triangle_type(a, b, c)}")


if __name__ == "__main__":
    main()
