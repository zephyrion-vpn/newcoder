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


def main() -> None:
    n = read_positive_int("Введите N: ")
    cubes = {number: number ** 3 for number in range(1, n + 1)}
    print(cubes)


if __name__ == "__main__":
    main()
