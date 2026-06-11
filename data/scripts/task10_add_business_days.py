from datetime import date, timedelta


def add_business_days(start: date, days: int) -> date:
    if days < 0:
        raise ValueError("Количество рабочих дней не может быть отрицательным.")
    current = start
    remaining = days
    while remaining > 0:
        current += timedelta(days=1)
        if current.weekday() < 5:
            remaining -= 1
    return current


def main() -> None:
    today = date.today()
    print(f"{today} + 5 рабочих дней = {add_business_days(today, 5)}")


if __name__ == "__main__":
    main()
