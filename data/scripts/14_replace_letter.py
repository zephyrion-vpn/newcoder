def replace_a_with_o(text: str) -> str:
    return text.replace("а", "о").replace("А", "О")


def main() -> None:
    text = input("Введите текст: ")
    print(replace_a_with_o(text))


if __name__ == "__main__":
    main()
