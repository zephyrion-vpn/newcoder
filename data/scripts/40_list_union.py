def main() -> None:
    first = [1, 2, 3]
    second = [3, 4, 5]
    print(list(dict.fromkeys(first + second)))


if __name__ == "__main__":
    main()
