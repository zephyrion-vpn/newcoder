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


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def main() -> None:
    a = read_int("Введите первое число: ")
    b = read_int("Введите второе число: ")
    print(f"НОК: {lcm(a, b)}")


if __name__ == "__main__":
    main()
