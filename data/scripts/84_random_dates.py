import random
from datetime import date, timedelta


def random_dates_in_year(year: int, count: int) -> list[date]:
    start = date(year, 1, 1)
    days_in_year = (date(year + 1, 1, 1) - start).days
    offsets = random.sample(range(days_in_year), min(count, days_in_year))
    return sorted(start + timedelta(days=offset) for offset in offsets)


def main() -> None:
    year = date.today().year
    for value in random_dates_in_year(year, 5):
        print(value.isoformat())


if __name__ == "__main__":
    main()
