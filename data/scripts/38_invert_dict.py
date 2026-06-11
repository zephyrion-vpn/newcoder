def invert(data: dict) -> dict:
    inverted = {value: key for key, value in data.items()}
    if len(inverted) != len(data):
        raise ValueError("Значения словаря не уникальны, инверсия невозможна без потерь.")
    return inverted


def main() -> None:
    data = {"a": 1, "b": 2, "c": 3}
    print(f"Исходный словарь: {data}")
    print(f"Перевёрнутый: {invert(data)}")


if __name__ == "__main__":
    main()
