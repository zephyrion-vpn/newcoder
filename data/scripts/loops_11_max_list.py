def main() -> None:
    items = [3, 7, 2, 9, 5]
    maximum = items[0]
    for item in items:
        if item > maximum:
            maximum = item
    print(maximum)


if __name__ == "__main__":
    main()
