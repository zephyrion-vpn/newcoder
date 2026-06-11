def main() -> None:
    first = [1, 2, 3]
    second = [2, 3, 4]
    common = set(second)
    print([value for value in first if value in common])


if __name__ == "__main__":
    main()
