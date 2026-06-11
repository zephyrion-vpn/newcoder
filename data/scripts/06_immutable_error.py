def main() -> None:
    data = (1, 2, 3)
    try:
        data[0] = 10
    except TypeError as error:
        print(f"TypeError: {error}")


if __name__ == "__main__":
    main()
