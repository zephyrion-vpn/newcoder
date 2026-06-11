import string

ALPHABET = string.ascii_lowercase
N = len(ALPHABET)


def _shift_char(char: str, key_char: str, decrypt: bool) -> str:
    base = ord("A") if char.isupper() else ord("a")
    offset = ALPHABET.index(key_char.lower())
    if decrypt:
        offset = -offset
    return chr((ord(char.lower()) - ord("a") + offset) % N + base)


def vigenere(text: str, key: str, decrypt: bool = False) -> str:
    if not key.isalpha():
        raise ValueError("Ключ должен состоять только из букв.")
    result: list[str] = []
    key_index = 0
    for char in text:
        if char.isalpha() and char.isascii():
            key_char = key[key_index % len(key)]
            result.append(_shift_char(char, key_char, decrypt))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)


def main() -> None:
    message = "Attack at Dawn!"
    key = "LEMON"
    encrypted = vigenere(message, key)
    decrypted = vigenere(encrypted, key, decrypt=True)
    print(f"Исходный:    {message}")
    print(f"Шифр:       {encrypted}")
    print(f"Расшифровка: {decrypted}")
    print(f"Совпадает: {decrypted == message}")


if __name__ == "__main__":
    main()
