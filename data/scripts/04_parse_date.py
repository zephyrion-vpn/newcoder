from datetime import date, datetime


def parse_date(text: str, fmt: str = "%d.%m.%Y") -> date:
    return datetime.strptime(text.strip(), fmt).date()


def prompt_date(fmt: str = "%d.%m.%Y") -> date:
    while True:
        try:
            raw = input(f"Введите дату ({fmt}): ")
        except EOFError:
            raise SystemExit("\nВвод завершён.")
        try:
            return parse_date(raw, fmt)
        except ValueError:
            print("Неверный формат даты, попробуйте снова.")


def main() -> None:
    result = prompt_date()
    print(f"Распознана дата: {result.isoformat()}")


if __name__ == "__main__":
    main()
