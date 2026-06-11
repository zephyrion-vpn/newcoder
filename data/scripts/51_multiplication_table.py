def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")


def main() -> None:
    number = read_int("Введите число: ")
    for multiplier in range(1, 11):
        print(f"{number} × {multiplier} = {number * multiplier}")


if __name__ == "__main__":
    main()
