def main() -> None:
    items = [1, 2, 3, 4]
    reversed_items = []
    for item in items:
        reversed_items.insert(0, item)
    print(reversed_items)


if __name__ == "__main__":
    main()
