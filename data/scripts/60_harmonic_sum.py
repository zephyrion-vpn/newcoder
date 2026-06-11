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


def harmonic_sum(n: int) -> float:
    return sum(1 / k for k in range(1, n + 1))


def main() -> None:
    n = read_positive_int("Введите N: ")
    print(f"Сумма ряда: {harmonic_sum(n)}")


if __name__ == "__main__":
    main()
