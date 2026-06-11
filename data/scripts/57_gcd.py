def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")


def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def main() -> None:
    a = read_int("Введите первое число: ")
    b = read_int("Введите второе число: ")
    if a == 0 and b == 0:
        print("НОД(0, 0) не определён.")
    else:
        print(f"НОД: {gcd(a, b)}")


if __name__ == "__main__":
    main()
