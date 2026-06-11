def main() -> None:
    data = {"a": 3, "b": 1, "c": 2}
    print(dict(sorted(data.items(), key=lambda item: item[1])))


if __name__ == "__main__":
    main()
