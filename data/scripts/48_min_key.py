def main() -> None:
    data = {"a": 1, "b": 3, "c": 2}
    print(min(data, key=data.get))


if __name__ == "__main__":
    main()
