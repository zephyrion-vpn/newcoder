def main() -> None:
    items = [4, -2, 7, -5, 1]
    total = 0
    for item in items:
        if item > 0:
            total += item
    print(total)


if __name__ == "__main__":
    main()
