def main() -> None:
    filename = input("Введите имя файла: ").strip()
    try:
        with open(filename, encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}: {line.rstrip(chr(10))}")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except OSError as error:
        print(f"Не удалось прочитать файл: {error}")


if __name__ == "__main__":
    main()
