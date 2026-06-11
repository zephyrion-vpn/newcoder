def main() -> None:
    try:
        value = int("42")
    except ValueError:
        print("invalid")
    else:
        print(value)


if __name__ == "__main__":
    main()
