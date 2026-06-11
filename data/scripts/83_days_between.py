from datetime import date


def read_date(prompt: str) -> date:
    while True:
        raw = input(prompt).strip()
        try:
            return date.fromisoformat(raw)
        except ValueError:
            print("Введите дату в формате ГГГГ-ММ-ДД.")


def main() -> None:
    first = read_date("Первая дата (ГГГГ-ММ-ДД): ")
    second = read_date("Вторая дата (ГГГГ-ММ-ДД): ")
    print(f"Разница в днях: {abs((second - first).days)}")


if __name__ == "__main__":
    main()
