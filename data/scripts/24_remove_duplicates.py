def read_items(prompt: str) -> list[str]:
    items = input(prompt).split()
    if not items:
        raise SystemExit("Список не может быть пустым.")
    return items


def remove_duplicates(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def main() -> None:
    items = read_items("Введите элементы через пробел: ")
    print(f"Без дубликатов: {remove_duplicates(items)}")


if __name__ == "__main__":
    main()
