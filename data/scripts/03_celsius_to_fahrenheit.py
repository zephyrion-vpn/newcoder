def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите корректное число.")


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def main() -> None:
    celsius = read_number("Введите температуру в градусах Цельсия: ")
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} °C = {fahrenheit} °F")


if __name__ == "__main__":
    main()
