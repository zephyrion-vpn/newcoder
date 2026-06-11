def main() -> None:
    data = {"a": 1, "b": 2}
    print({value: key for key, value in data.items()})


if __name__ == "__main__":
    main()
