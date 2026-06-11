def read_integers(prompt: str) -> list[int]:
    while True:
        raw = input(prompt).strip()
        parts = raw.replace(",", " ").split()
        if not parts:
            print("Список не может быть пустым.")
            continue
        try:
            return [int(part) for part in parts]
        except ValueError:
            print("Введите только целые числа.")


def main() -> None:
    numbers = read_integers("Введите целые числа через пробел: ")
    total = sum(number for number in numbers if number % 2 == 0)
    print(f"Сумма чётных: {total}")


if __name__ == "__main__":
    main()
