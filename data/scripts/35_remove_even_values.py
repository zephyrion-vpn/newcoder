def remove_even_values(data: dict[str, int]) -> dict[str, int]:
    return {key: value for key, value in data.items() if value % 2 != 0}


def main() -> None:
    data = {"a": 1, "b": 2, "c": 3, "d": 4}
    print(f"Исходный словарь: {data}")
    print(f"Без чётных значений: {remove_even_values(data)}")


if __name__ == "__main__":
    main()
