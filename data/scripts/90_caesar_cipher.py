def shift_char(char: str, shift: int, base: str, size: int) -> str:
    return chr((ord(char) - ord(base) + shift) % size + ord(base))


def caesar_encrypt(text: str, shift: int) -> str:
    result = []
    for char in text:
        if "a" <= char <= "z":
            result.append(shift_char(char, shift, "a", 26))
        elif "A" <= char <= "Z":
            result.append(shift_char(char, shift, "A", 26))
        elif "а" <= char <= "я" or char == "ё":
            normalized = "е" if char == "ё" else char
            result.append(shift_char(normalized, shift, "а", 32))
        elif "А" <= char <= "Я" or char == "Ё":
            normalized = "Е" if char == "Ё" else char
            result.append(shift_char(normalized, shift, "А", 32))
        else:
            result.append(char)
    return "".join(result)


def read_shift(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")


def main() -> None:
    text = input("Введите текст: ")
    shift = read_shift("Сдвиг N: ")
    print(f"Зашифровано: {caesar_encrypt(text, shift)}")


if __name__ == "__main__":
    main()
