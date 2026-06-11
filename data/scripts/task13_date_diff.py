import calendar
from datetime import date


def date_diff(start: date, end: date) -> tuple[int, int, int]:
    if end < start:
        start, end = end, start
    years = end.year - start.year
    months = end.month - start.month
    days = end.day - start.day
    if days < 0:
        months -= 1
        prev_month = 12 if end.month == 1 else end.month - 1
        prev_year = end.year - 1 if end.month == 1 else end.year
        days += calendar.monthrange(prev_year, prev_month)[1]
    if months < 0:
        years -= 1
        months += 12
    return years, months, days


def main() -> None:
    start = date(1990, 3, 15)
    end = date(2026, 6, 10)
    years, months, days = date_diff(start, end)
    print(f"Между {start} и {end}: {years} лет, {months} месяцев, {days} дней")


if __name__ == "__main__":
    main()
