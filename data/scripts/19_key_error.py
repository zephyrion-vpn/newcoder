def main() -> None:
    data: dict[str, int] = {}
    try:
        data["missing"]
    except KeyError as error:
        print(f"KeyError: {error}")


if __name__ == "__main__":
    main()
