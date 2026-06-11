def read_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")
            continue
        if value < 1:
            print("Размер должен быть не меньше 1.")
            continue
        return value


def main() -> None:
    width = read_positive_int("Введите ширину: ")
    height = read_positive_int("Введите высоту: ")
    for _ in range(height):
        print("*" * width)


if __name__ == "__main__":
    main()
