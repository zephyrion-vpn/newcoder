def main() -> None:
    number = 5
    factorial = 1
    for value in range(2, number + 1):
        factorial *= value
    print(factorial)


if __name__ == "__main__":
    main()
