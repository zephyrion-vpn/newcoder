import tempfile
from pathlib import Path


def xor_bytes(data: bytes, key: bytes) -> bytes:
    if not key:
        raise ValueError("Ключ не может быть пустым.")
    return bytes(byte ^ key[i % len(key)] for i, byte in enumerate(data))


def encrypt_file(source: Path, key: bytes) -> Path:
    data = source.read_bytes()
    encrypted = xor_bytes(data, key)
    target = source.with_suffix(source.suffix + ".enc")
    target.write_bytes(encrypted)
    return target


def decrypt_file(enc_path: Path, key: bytes) -> bytes:
    return xor_bytes(enc_path.read_bytes(), key)


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    source = tmp / "secret.txt"
    original_text = "Секретное сообщение: пароль 12345"
    source.write_text(original_text, encoding="utf-8")
    key = b"my-secret-key"

    enc_path = encrypt_file(source, key)
    print(f"Зашифровано в: {enc_path.name}")
    print(f"Зашифрованные байты отличаются: {enc_path.read_bytes() != source.read_bytes()}")

    decrypted = decrypt_file(enc_path, key).decode("utf-8")
    print(f"Расшифровано: {decrypted}")
    print(f"Совпадает с исходным: {decrypted == original_text}")


if __name__ == "__main__":
    main()
