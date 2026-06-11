def main() -> None:
    while True:
        command = input("Введите команду (stop для выхода): ").strip().lower()
        if command == "stop":
            break
    print("Получена команда stop")


if __name__ == "__main__":
    main()
