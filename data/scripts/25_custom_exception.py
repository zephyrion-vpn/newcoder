class MyError(Exception):
    pass


def main() -> None:
    try:
        raise MyError("custom")
    except MyError as error:
        print(error)


if __name__ == "__main__":
    main()
