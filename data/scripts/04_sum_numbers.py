import re

NUMBER_PATTERN = re.compile(r"-?\d+(?:\.\d+)?")


def extract_numbers(text: str) -> list[float]:
    return [float(token) for token in NUMBER_PATTERN.findall(text)]


def main() -> None:
    text = "Температура -5.5, баланс 100, скидка -10, пи 3.14."
    numbers = extract_numbers(text)
    print(numbers)
    print(f"Сумма: {sum(numbers)}")


if __name__ == "__main__":
    main()
