import json


def main() -> None:
    filename = input("Введите имя JSON-файла: ").strip()
    try:
        with open(filename, encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return
    except json.JSONDecodeError as error:
        print(f"Некорректный JSON: {error}")
        return

    if not isinstance(data, dict) or "price" not in data:
        print("В файле нет поля 'price'.")
        return

    try:
        new_price = float(input("Введите новую цену: ").strip().replace(",", "."))
    except ValueError:
        print("Цена должна быть числом.")
        return

    data["price"] = new_price
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
    print("Цена обновлена.")


if __name__ == "__main__":
    main()
