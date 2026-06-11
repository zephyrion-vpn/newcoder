def binary_to_decimal(binary: str) -> int:
    result = 0
    for char in binary:
        if char not in "01":
            raise ValueError("Двоичное число содержит только 0 и 1.")
        result = result * 2 + (1 if char == "1" else 0)
    return result


def main() -> None:
    binary = input("Введите двоичное число: ").strip()
    if not binary:
        print("Пустая строка.")
        return
    try:
        print(f"Десятичное: {binary_to_decimal(binary)}")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
