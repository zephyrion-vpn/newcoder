def with_item(items: list[int], value: int) -> list[int]:
    return items + [value]


if __name__ == "__main__":
    numbers = [1, 2]
    print(with_item(numbers, 3))
    print(numbers)
