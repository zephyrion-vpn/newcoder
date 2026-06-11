from math import factorial


def read_non_negative_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")
            continue
        if value < 0:
            print("Факториал определён только для неотрицательных чисел.")
            continue
        return value


def main() -> None:
    number = read_non_negative_int("Введите число: ")
    print(f"{number}! = {factorial(number)}")


if __name__ == "__main__":
    main()
