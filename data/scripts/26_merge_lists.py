def read_items(prompt: str) -> list[str]:
    return input(prompt).split()


def main() -> None:
    first = read_items("Введите элементы первого списка: ")
    second = read_items("Введите элементы второго списка: ")
    merged = first + second
    print(f"Объединённый список: {merged}")
    print(f"Длина: {len(merged)}")


if __name__ == "__main__":
    main()
