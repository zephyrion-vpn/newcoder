def read_name(prompt: str = "Введите ваше имя: ") -> str:
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Имя не может быть пустым. Попробуйте ещё раз.")


def main() -> None:
    name = read_name()
    print(f"Привет, {name}!")


if __name__ == "__main__":
    main()
