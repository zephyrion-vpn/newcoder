import calendar
from datetime import date


def _days_in_month(year: int, month: int) -> int:
    return calendar.monthrange(year, month)[1]


def date_difference(start: date, end: date) -> tuple[int, int, int]:
    if end < start:
        start, end = end, start
    years = end.year - start.year
    months = end.month - start.month
    days = end.day - start.day
    if days < 0:
        months -= 1
        borrow_month = 12 if end.month == 1 else end.month - 1
        borrow_year = end.year - 1 if end.month == 1 else end.year
        days += _days_in_month(borrow_year, borrow_month)
    if months < 0:
        years -= 1
        months += 12
    return years, months, days


def main() -> None:
    start = date(1990, 5, 20)
    end = date.today()
    years, months, days = date_difference(start, end)
    print(f"С {start} по {end}: {years} лет, {months} месяцев, {days} дней")


if __name__ == "__main__":
    main()
