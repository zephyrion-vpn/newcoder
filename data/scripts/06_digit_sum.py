def read_three_digit_number() -> int:
    while True:
        raw = input("Введите трехзначное число: ").strip()
        try:
            number = int(raw)
        except ValueError:
            print("Введите целое число.")
            continue
        if 100 <= abs(number) <= 999:
            return number
        print("Число должно быть трехзначным.")


def digit_sum(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))


def main() -> None:
    number = read_three_digit_number()
    print(f"Сумма цифр: {digit_sum(number)}")


if __name__ == "__main__":
    main()
