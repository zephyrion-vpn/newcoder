def main() -> None:
    try:
        print(1 / 0)
    except ZeroDivisionError as error:
        print(f"ZeroDivisionError: {error}")


if __name__ == "__main__":
    main()
