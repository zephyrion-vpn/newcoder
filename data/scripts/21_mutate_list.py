def append_item(items: list[int], value: int) -> None:
    items.append(value)


if __name__ == "__main__":
    numbers = [1, 2]
    append_item(numbers, 3)
    print(numbers)
