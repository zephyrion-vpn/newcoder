def read_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")
            continue
        if value < 1:
            print("Число должно быть не меньше 1.")
            continue
        return value


def fibonacci(count: int) -> list[int]:
    sequence: list[int] = []
    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def main() -> None:
    count = read_positive_int("Введите N: ")
    print(fibonacci(count))


if __name__ == "__main__":
    main()
