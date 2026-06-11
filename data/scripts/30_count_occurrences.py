def read_integers(prompt: str) -> list[int]:
    while True:
        raw = input(prompt).strip()
        parts = raw.replace(",", " ").split()
        if not parts:
            print("Список не может быть пустым.")
            continue
        try:
            return [int(part) for part in parts]
        except ValueError:
            print("Введите только целые числа.")


def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")


def main() -> None:
    numbers = read_integers("Введите целые числа через пробел: ")
    target = read_integer("Введите число для поиска: ")
    print(f"Встречается раз: {numbers.count(target)}")


if __name__ == "__main__":
    main()
