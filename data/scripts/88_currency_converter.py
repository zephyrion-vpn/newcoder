RATES_TO_USD = {
    "USD": 1.0,
    "EUR": 1.08,
    "RUB": 0.011,
}


def convert(amount: float, source: str, target: str) -> float:
    return amount * RATES_TO_USD[source] / RATES_TO_USD[target]


def read_currency(prompt: str) -> str:
    while True:
        currency = input(prompt).strip().upper()
        if currency in RATES_TO_USD:
            return currency
        print(f"Доступные валюты: {', '.join(RATES_TO_USD)}.")


def read_amount(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите корректное число.")
            continue
        if value < 0:
            print("Сумма не может быть отрицательной.")
            continue
        return value


def main() -> None:
    source = read_currency(f"Валюта ({', '.join(RATES_TO_USD)}): ")
    amount = read_amount("Сумма: ")
    for target in RATES_TO_USD:
        if target != source:
            print(f"{amount} {source} = {convert(amount, source, target):.2f} {target}")


if __name__ == "__main__":
    main()
