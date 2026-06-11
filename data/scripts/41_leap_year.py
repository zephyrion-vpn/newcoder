def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main() -> None:
    year = read_int("Введите год: ")
    print("Високосный." if is_leap_year(year) else "Невисокосный.")


if __name__ == "__main__":
    main()
