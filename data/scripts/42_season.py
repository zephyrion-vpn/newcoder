SEASONS = {
    12: "Зима", 1: "Зима", 2: "Зима",
    3: "Весна", 4: "Весна", 5: "Весна",
    6: "Лето", 7: "Лето", 8: "Лето",
    9: "Осень", 10: "Осень", 11: "Осень",
}


def read_month(prompt: str) -> int:
    while True:
        try:
            month = int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")
            continue
        if 1 <= month <= 12:
            return month
        print("Номер месяца должен быть от 1 до 12.")


def main() -> None:
    month = read_month("Введите номер месяца: ")
    print(f"Время года: {SEASONS[month]}")


if __name__ == "__main__":
    main()
