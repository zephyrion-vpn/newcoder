from datetime import date


def days_until_birthday(birth_date: date, today: date | None = None) -> int:
    today = today or date.today()
    try:
        next_birthday = birth_date.replace(year=today.year)
    except ValueError:
        next_birthday = date(today.year, 3, 1)
    if next_birthday < today:
        try:
            next_birthday = birth_date.replace(year=today.year + 1)
        except ValueError:
            next_birthday = date(today.year + 1, 3, 1)
    return (next_birthday - today).days


def read_birth_date(prompt: str) -> date:
    while True:
        raw = input(prompt).strip()
        try:
            return date.fromisoformat(raw)
        except ValueError:
            print("Введите дату в формате ГГГГ-ММ-ДД.")


def main() -> None:
    birth_date = read_birth_date("Введите дату рождения (ГГГГ-ММ-ДД): ")
    remaining = days_until_birthday(birth_date)
    print("Сегодня День рождения!" if remaining == 0 else f"До следующего Дня рождения: {remaining} дн.")


if __name__ == "__main__":
    main()
