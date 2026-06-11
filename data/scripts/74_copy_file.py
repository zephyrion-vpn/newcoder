import shutil


def main() -> None:
    source = input("Введите имя исходного файла: ").strip()
    destination = input("Введите имя файла-приёмника: ").strip()
    try:
        shutil.copyfile(source, destination)
    except FileNotFoundError:
        print(f"Исходный файл '{source}' не найден.")
    except shutil.SameFileError:
        print("Исходный файл и приёмник совпадают.")
    except OSError as error:
        print(f"Не удалось скопировать файл: {error}")
    else:
        print(f"Содержимое скопировано в '{destination}'.")


if __name__ == "__main__":
    main()
