import random


def random_filtered(n: int, low: int = 1, high: int = 100) -> list[int]:
    if n < 0:
        raise ValueError("Количество не может быть отрицательным.")
    result: list[int] = []
    while len(result) < n:
        number = random.randint(low, high)
        if number % 3 != 0 and number % 5 != 0:
            result.append(number)
    return result


def main() -> None:
    numbers = random_filtered(10)
    print(numbers)
    print(all(x % 3 != 0 and x % 5 != 0 for x in numbers))


if __name__ == "__main__":
    main()
