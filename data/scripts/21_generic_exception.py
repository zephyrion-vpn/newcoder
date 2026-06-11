def main() -> None:
    try:
        1 / 0
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
