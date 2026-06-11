def read_integers(prompt: str) -> set[int]:
    while True:
        raw = input(prompt).strip()
        parts = raw.replace(",", " ").split()
        if not parts:
            print("Множество не может быть пустым.")
            continue
        try:
            return {int(part) for part in parts}
        except ValueError:
            print("Введите только целые числа.")


def main() -> None:
    numbers = read_integers("Введите целые числа через пробел: ")
    divisible = {number for number in numbers if number % 3 == 0}
    print(f"Делятся на 3: {divisible}")


if __name__ == "__main__":
    main()
