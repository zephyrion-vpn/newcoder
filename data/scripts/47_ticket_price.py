FULL_PRICE = 500.0


def read_age(prompt: str) -> int:
    while True:
        try:
            age = int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")
            continue
        if age < 0:
            print("Возраст не может быть отрицательным.")
            continue
        return age


def ticket_price(age: int, full_price: float) -> float:
    if age < 7:
        return 0.0
    if age < 18:
        return full_price * 0.5
    return full_price


def main() -> None:
    age = read_age("Введите возраст: ")
    print(f"Стоимость билета: {ticket_price(age, FULL_PRICE):.2f}")


if __name__ == "__main__":
    main()
