def read_amount(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите корректное число.")
            continue
        if value < 0:
            print("Значение не может быть отрицательным.")
            continue
        return value


def main() -> None:
    bill = read_amount("Введите сумму чека: ")
    tip_percent = read_amount("Введите процент чаевых: ")

    tip = bill * tip_percent / 100
    total = bill + tip

    print(f"Чаевые: {tip:.2f}")
    print(f"Итого к оплате: {total:.2f}")


if __name__ == "__main__":
    main()
