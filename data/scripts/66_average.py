def average(*args: float) -> float:
    if not args:
        raise ValueError("Нужен хотя бы один аргумент.")
    return sum(args) / len(args)


def main() -> None:
    print(average(2, 4, 6))
    print(average(10, 20, 30, 40))
    print(average(5))


if __name__ == "__main__":
    main()
