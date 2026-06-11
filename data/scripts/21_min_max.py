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
            print("Введите только числа, разделённые пробелами.")


def find_min_max(numbers: list[float]) -> tuple[float, float]:
    minimum = maximum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number
    return minimum, maximum


def main() -> None:
    numbers = read_numbers("Введите числа через пробел: ")
    minimum, maximum = find_min_max(numbers)
    print(f"Минимум: {minimum}")
    print(f"Максимум: {maximum}")


if __name__ == "__main__":
    main()
