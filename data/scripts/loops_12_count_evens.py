def main() -> None:
    items = [1, 2, 3, 4, 5, 6]
    count = 0
    for item in items:
        if item % 2 == 0:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
