import csv


def main() -> None:
    filename = input("Введите имя CSV-файла: ").strip()
    try:
        with open(filename, encoding="utf-8", newline="") as file:
            rows = list(csv.reader(file))
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return
    except OSError as error:
        print(f"Не удалось прочитать файл: {error}")
        return

    if not rows:
        print("Файл пустой.")
        return

    widths = [max(len(row[i]) for row in rows if i < len(row)) for i in range(len(rows[0]))]
    for row in rows:
        print(" | ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)))


if __name__ == "__main__":
    main()
