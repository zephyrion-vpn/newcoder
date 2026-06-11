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


def insertion_sort(numbers: list[float]) -> list[float]:
    result = numbers[:]
    for i in range(1, len(result)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result


def main() -> None:
    numbers = read_numbers("Введите числа через пробел: ")
    print(f"Отсортировано: {insertion_sort(numbers)}")


if __name__ == "__main__":
    main()
