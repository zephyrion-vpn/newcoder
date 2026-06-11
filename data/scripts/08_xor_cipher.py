import os
import tempfile


def xor_bytes(data: bytes, key: int) -> bytes:
    return bytes(byte ^ key for byte in data)


def encrypt_file(source: str, key: int) -> str:
    if not 0 <= key <= 255:
        raise ValueError("Ключ должен быть байтом (0–255).")
    destination = source + ".enc"
    with open(source, "rb") as handle:
        data = handle.read()
    with open(destination, "wb") as handle:
        handle.write(xor_bytes(data, key))
    return destination


def main() -> None:
    folder = tempfile.mkdtemp()
    source = os.path.join(folder, "secret.txt")
    original = "Секретное сообщение"
    with open(source, "w", encoding="utf-8") as handle:
        handle.write(original)
    encrypted = encrypt_file(source, key=42)
    with open(encrypted, "rb") as handle:
        decrypted = xor_bytes(handle.read(), 42).decode("utf-8")
    print(f"Зашифровано в: {os.path.basename(encrypted)}")
    print(f"Расшифровка совпадает: {decrypted == original}")


if __name__ == "__main__":
    main()
