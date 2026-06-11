def main() -> None:
    number = 5
    factorial = 1
    value = 2
    while value <= number:
        factorial *= value
        value += 1
    print(factorial)


if __name__ == "__main__":
    main()
