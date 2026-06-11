def read_numbers(prompt: str) -> list[float]:
    while True:
        raw = input(prompt).strip()
        parts = raw.replace(",", " ").split()
        if not parts:
            print("Список не может быть пустым.")
            continue
        try:
            return [float(part) for part in parts]
        except ValueError:
            print("Введите только числа.")


def second_largest(numbers: list[float]) -> float | None:
    unique = sorted(set(numbers), reverse=True)
    return unique[1] if len(unique) >= 2 else None


def main() -> None:
    numbers = read_numbers("Введите числа через пробел: ")
    result = second_largest(numbers)
    if result is None:
        print("В списке недостаточно различных значений.")
    else:
        print(f"Второй по величине: {result}")


if __name__ == "__main__":
    main()
