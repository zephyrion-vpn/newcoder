def main() -> None:
    items = [3, 7, 9, 2]
    target = 9
    for index, value in enumerate(items):
        if value == target:
            print(index)
            break


if __name__ == "__main__":
    main()
