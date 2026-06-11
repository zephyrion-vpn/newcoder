def read_number_in_range(prompt: str, low: int, high: int) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")
            continue
        if low <= value <= high:
            return value
        print(f"Число должно быть от {low} до {high}.")


def main() -> None:
    number = read_number_in_range("Введите число от 1 до 100: ", 1, 100)
    print("Чётное." if number % 2 == 0 else "Нечётное.")


if __name__ == "__main__":
    main()
