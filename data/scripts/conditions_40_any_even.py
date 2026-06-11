def main() -> None:
    items = [1, 3, 5, 6]
    print(any(item % 2 == 0 for item in items))


if __name__ == "__main__":
    main()
