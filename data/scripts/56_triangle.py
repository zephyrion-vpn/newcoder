def read_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")
            continue
        if value < 1:
            print("Высота должна быть не меньше 1.")
            continue
        return value


def main() -> None:
    height = read_positive_int("Введите высоту ёлочки: ")
    for row in range(1, height + 1):
        stars = 2 * row - 1
        print(" " * (height - row) + "*" * stars)


if __name__ == "__main__":
    main()
