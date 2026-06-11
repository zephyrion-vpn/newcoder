def main() -> None:
    items = [3, -1, 4, -2, 5]
    for item in items:
        if item < 0:
            continue
        print(item)


if __name__ == "__main__":
    main()
