import calendar


def month_calendar(year: int, month: int) -> str:
    if not 1 <= month <= 12:
        raise ValueError("Месяц должен быть в диапазоне 1–12.")
    return calendar.month(year, month)


def main() -> None:
    print(month_calendar(2026, 6), end="")


if __name__ == "__main__":
    main()
