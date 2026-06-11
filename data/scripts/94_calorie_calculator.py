CALORIES_PER_100G = {
    "яблоко": 52,
    "банан": 89,
    "курица": 165,
    "рис": 130,
    "хлеб": 265,
}


def read_grams(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите корректное число.")
            continue
        if value < 0:
            print("Масса не может быть отрицательной.")
            continue
        return value


def main() -> None:
    print(f"Доступные продукты: {', '.join(CALORIES_PER_100G)}.")
    print("Пустая строка завершает ввод.")
    total = 0.0
    while True:
        product = input("Продукт: ").strip().lower()
        if not product:
            break
        if product not in CALORIES_PER_100G:
            print("Нет такого продукта в справочнике.")
            continue
        grams = read_grams("Масса (г): ")
        total += CALORIES_PER_100G[product] * grams / 100
    print(f"Итого калорий: {total:.1f}")


if __name__ == "__main__":
    main()
