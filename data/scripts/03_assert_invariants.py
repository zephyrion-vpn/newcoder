from numbers import Number


def average(numbers: list[float]) -> float:
    assert numbers, "Список не должен быть пустым."
    assert all(isinstance(x, Number) and not isinstance(x, bool) for x in numbers), \
        "Все элементы должны быть числами."
    return sum(numbers) / len(numbers)


def main() -> None:
    print(average([2, 4, 6]))
    for bad in ([], [1, "2", 3]):
        try:
            average(bad)  # type: ignore[arg-type]
        except AssertionError as error:
            print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
