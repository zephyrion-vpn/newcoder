from datetime import date, datetime


def calculate_age(birth: str, fmt: str = "%d.%m.%Y") -> int:
    birth_date = datetime.strptime(birth.strip(), fmt).date()
    today = date.today()
    if birth_date > today:
        raise ValueError("Дата рождения не может быть в будущем.")
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def main() -> None:
    for birth in ("15.01.1990", "31.12.2000", "10.06.2020"):
        print(f"{birth} → {calculate_age(birth)} лет")


if __name__ == "__main__":
    main()
