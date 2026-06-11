def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите корректное число.")


def main() -> None:
    dividend = read_number("Введите делимое: ")
    divisor = read_number("Введите делитель: ")
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно.")
    else:
        print(f"Результат: {result}")


if __name__ == "__main__":
    main()
