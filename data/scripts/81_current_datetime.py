from datetime import datetime


def main() -> None:
    print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))


if __name__ == "__main__":
    main()
