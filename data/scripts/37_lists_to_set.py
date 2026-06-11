def read_items(prompt: str) -> list[str]:
    return input(prompt).split()


def main() -> None:
    first = read_items("Введите элементы первого списка: ")
    second = read_items("Введите элементы второго списка: ")
    unique = set(first) | set(second)
    print(f"Множество без дубликатов: {unique}")


if __name__ == "__main__":
    main()
