def main() -> None:
    filename = input("Введите имя файла: ").strip()
    try:
        with open(filename, encoding="utf-8") as file:
            words = file.read().split()
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return
    except OSError as error:
        print(f"Не удалось прочитать файл: {error}")
        return

    if not words:
        print("Файл пустой.")
        return
    print(f"Самое длинное слово: {max(words, key=len)}")


if __name__ == "__main__":
    main()
