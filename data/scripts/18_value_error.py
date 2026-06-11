def main() -> None:
    try:
        int("abc")
    except ValueError as error:
        print(f"ValueError: {error}")


if __name__ == "__main__":
    main()
