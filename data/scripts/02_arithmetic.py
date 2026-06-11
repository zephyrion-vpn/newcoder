def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите корректное число.")


def main() -> None:
    a = read_number("Введите первое число: ")
    b = read_number("Введите второе число: ")

    print(f"Сумма: {a + b}")
    print(f"Разность: {a - b}")
    print(f"Произведение: {a * b}")

    if b == 0:
        print("Частное: деление на ноль невозможно")
    else:
        print(f"Частное: {a / b}")


if __name__ == "__main__":
    main()
