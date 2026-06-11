import sys
from datetime import date, datetime
from typing import Optional

DATE_FORMAT = "%Y-%m-%d"


def parse_date(text: str) -> date:
    return datetime.strptime(text.strip(), DATE_FORMAT).date()


def prompt_date(reader=input) -> Optional[date]:
    while True:
        try:
            raw = reader(f"Введите дату ({DATE_FORMAT}): ")
        except EOFError:
            print("\nВвод завершён.")
            return None
        try:
            return parse_date(raw)
        except ValueError:
            print(f"Неверный формат: {raw!r}. Попробуйте снова (например, 2026-06-10).")


def main() -> None:
    samples = iter(["не дата", "2026-13-40", "2026-06-10"])

    def fake_reader(_prompt: str) -> str:
        value = next(samples)
        print(f"{_prompt}{value}")
        return value

    result = prompt_date(reader=fake_reader)
    print(f"Распознана дата: {result}")
    if not sys.stdin.isatty():
        return
    print("Теперь вручную:")
    print("Итог:", prompt_date())


if __name__ == "__main__":
    main()
