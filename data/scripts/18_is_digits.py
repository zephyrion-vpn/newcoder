def main() -> None:
    text = input("Введите строку: ")
    if text.isdigit():
        print("Строка состоит только из цифр.")
    else:
        print("Строка содержит не только цифры.")


if __name__ == "__main__":
    main()
