def main() -> None:
    try:
        print(temp)
    except NameError as error:
        print(f"NameError: {error}")


if __name__ == "__main__":
    main()
