def key_with_max_value(data: dict[str, float]) -> str:
    return max(data, key=data.get)


def main() -> None:
    scores = {"Анна": 87, "Борис": 95, "Вера": 72}
    print(f"Словарь: {scores}")
    print(f"Ключ с максимальным значением: {key_with_max_value(scores)}")


if __name__ == "__main__":
    main()
