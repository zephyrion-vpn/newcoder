def main() -> None:
    filename = input("Введите имя файла: ").strip()
    try:
        with open(filename, encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return
    except OSError as error:
        print(f"Не удалось прочитать файл: {error}")
        return

    lines = text.splitlines()
    print(f"Строк: {len(lines)}")
    print(f"Слов: {len(text.split())}")
    print(f"Символов: {len(text)}")


if __name__ == "__main__":
    main()
