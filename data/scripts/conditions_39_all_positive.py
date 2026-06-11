def main() -> None:
    items = [1, 2, 3]
    print(all(item > 0 for item in items))


if __name__ == "__main__":
    main()
