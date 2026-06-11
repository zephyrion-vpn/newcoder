def _shift_char(char: str, key_char: str, decrypt: bool) -> tuple[str, bool]:
    if char.isupper():
        base = ord("A")
    elif char.islower():
        base = ord("a")
    else:
        return char, False
    shift = ord(key_char.lower()) - ord("a")
    if decrypt:
        shift = -shift
    return chr((ord(char) - base + shift) % 26 + base), True


def vigenere(text: str, key: str, decrypt: bool = False) -> str:
    if not key.isalpha():
        raise ValueError("Ключ должен состоять из букв")
    result: list[str] = []
    key_index = 0
    for char in text:
        shifted, consumed = _shift_char(char, key[key_index % len(key)], decrypt)
        result.append(shifted)
        if consumed:
            key_index += 1
    return "".join(result)


def main() -> None:
    text = "Attack at Dawn!"
    key = "LEMON"
    encrypted = vigenere(text, key)
    decrypted = vigenere(encrypted, key, decrypt=True)
    print("Исходный:", text)
    print("Шифр:    ", encrypted)
    print("Дешифр:  ", decrypted)


if __name__ == "__main__":
    main()
