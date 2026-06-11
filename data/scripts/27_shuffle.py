import random


def read_items(prompt: str) -> list[str]:
    items = input(prompt).split()
    if not items:
        raise SystemExit("Список не может быть пустым.")
    return items


def main() -> None:
    items = read_items("Введите элементы через пробел: ")
    shuffled = items[:]
    random.shuffle(shuffled)
    print(f"Перемешано: {shuffled}")


if __name__ == "__main__":
    main()
