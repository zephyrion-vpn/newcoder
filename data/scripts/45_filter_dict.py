def main() -> None:
    data = {"a": 1, "b": 2, "c": 3}
    print({key: value for key, value in data.items() if value > 1})


if __name__ == "__main__":
    main()
