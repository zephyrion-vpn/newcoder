from datetime import date, datetime

DATE_FORMAT = "%Y-%m-%d"


def calculate_age(birth_date_str: str, today: date | None = None) -> int:
    birth = datetime.strptime(birth_date_str.strip(), DATE_FORMAT).date()
    today = today or date.today()
    if birth > today:
        raise ValueError("дата рождения в будущем")
    age = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1
    return age


def main() -> None:
    reference = date(2026, 6, 10)
    samples = ["1990-06-10", "1990-06-11", "2000-01-01", "2026-06-10"]
    for birth in samples:
        age = calculate_age(birth, today=reference)
        print(f"Дата рождения {birth} -> возраст на {reference}: {age} лет")

    try:
        calculate_age("2030-01-01", today=reference)
    except ValueError as error:
        print(f"Ошибка (ожидаемо): {error}")


if __name__ == "__main__":
    main()
