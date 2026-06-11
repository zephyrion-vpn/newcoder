import re
from datetime import date

DATE_PATTERN = re.compile(r"\b(\d{2})\.(\d{2})\.(\d{4})\b")


def extract_valid_dates(text: str) -> list[str]:
    valid = []
    for day, month, year in DATE_PATTERN.findall(text):
        try:
            date(int(year), int(month), int(day))
        except ValueError:
            continue
        valid.append(f"{day}.{month}.{year}")
    return valid


def main() -> None:
    text = "Даты: 01.01.2023, 32.13.2023, 29.02.2024, 29.02.2023, 15.07.1999."
    print(extract_valid_dates(text))


if __name__ == "__main__":
    main()
