from datetime import datetime


def main() -> None:
    print(datetime.strptime("2024-01-15", "%Y-%m-%d"))


if __name__ == "__main__":
    main()
