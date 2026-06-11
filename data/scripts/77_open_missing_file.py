def main() -> None:
    filename = input("Введите имя файла: ").strip()
    try:
        with open(filename, encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Проверьте имя и путь.")
    except PermissionError:
        print(f"Нет прав на чтение файла '{filename}'.")
    except OSError as error:
        print(f"Не удалось открыть файл: {error}")


if __name__ == "__main__":
    main()
