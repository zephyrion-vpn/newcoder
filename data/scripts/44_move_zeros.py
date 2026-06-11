def main() -> None:
    numbers = [0, 1, 0, 2, 3]
    non_zero = [value for value in numbers if value != 0]
    print(non_zero + [0] * (len(numbers) - len(non_zero)))


if __name__ == "__main__":
    main()
