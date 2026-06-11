def main() -> None:
    try:
        [1, 2, 3][5]
    except IndexError as error:
        print(f"IndexError: {error}")


if __name__ == "__main__":
    main()
