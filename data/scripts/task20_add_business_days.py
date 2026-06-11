from datetime import date, timedelta


def add_business_days(start: date, days: int) -> date:
    if days < 0:
        raise ValueError("Количество дней должно быть неотрицательным")
    current = start
    added = 0
    while added < days:
        current += timedelta(days=1)
        if current.weekday() < 5:
            added += 1
    return current


def main() -> None:
    start = date(2026, 6, 10)
    for offset in (1, 5, 10):
        result = add_business_days(start, offset)
        print(f"{start} + {offset} раб. дней = {result} ({result:%A})")


if __name__ == "__main__":
    main()
