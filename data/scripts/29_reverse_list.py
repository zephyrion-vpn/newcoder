def read_items(prompt: str) -> list[str]:
    return input(prompt).split()


def main() -> None:
    items = read_items("Введите элементы через пробел: ")
    print(f"Развёрнутый список: {items[::-1]}")


if __name__ == "__main__":
    main()
