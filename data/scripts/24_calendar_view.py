import calendar


def render_month(year: int, month: int) -> str:
    if not 1 <= month <= 12:
        raise ValueError("месяц должен быть от 1 до 12")
    cal = calendar.TextCalendar(firstweekday=0)
    return cal.formatmonth(year, month)


def main() -> None:
    year, month = 2026, 6
    print(render_month(year, month))
    weekday, days = calendar.monthrange(year, month)
    print(f"В месяце {days} дней, 1-е число — {calendar.day_name[weekday]}.")
    print(f"Год {year} високосный: {calendar.isleap(year)}")


if __name__ == "__main__":
    main()
