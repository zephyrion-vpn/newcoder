import base64
import hashlib
import hmac
import json
import os
import tempfile
from typing import Optional


def _derive_key(master: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", master.encode("utf-8"), salt, 100_000)


def _xor(data: bytes, key: bytes) -> bytes:
    full = (key * (len(data) // len(key) + 1))[: len(data)]
    return bytes(b ^ k for b, k in zip(data, full))


def save_vault(passwords: dict[str, str], master: str, path: str) -> None:
    salt = os.urandom(16)
    key = _derive_key(master, salt)
    plaintext = json.dumps(passwords, ensure_ascii=False).encode("utf-8")
    ciphertext = _xor(plaintext, key)
    mac = hmac.new(key, ciphertext, hashlib.sha256).digest()
    blob = {
        "salt": base64.b64encode(salt).decode(),
        "mac": base64.b64encode(mac).decode(),
        "data": base64.b64encode(ciphertext).decode(),
    }
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(blob, handle)


def load_vault(master: str, path: str) -> Optional[dict[str, str]]:
    with open(path, encoding="utf-8") as handle:
        blob = json.load(handle)
    salt = base64.b64decode(blob["salt"])
    ciphertext = base64.b64decode(blob["data"])
    expected_mac = base64.b64decode(blob["mac"])
    key = _derive_key(master, salt)
    actual_mac = hmac.new(key, ciphertext, hashlib.sha256).digest()
    if not hmac.compare_digest(expected_mac, actual_mac):
        return None
    plaintext = _xor(ciphertext, key)
    return json.loads(plaintext.decode("utf-8"))


def main() -> None:
    path = os.path.join(tempfile.mkdtemp(), "vault.json")
    secrets = {"github.com": "hunter2", "mail.ru": "qwerty123"}
    save_vault(secrets, "master-pass", path)
    print("Хранилище зашифровано и сохранено.")
    print("Неверный мастер-пароль:", load_vault("wrong", path))
    print("Верный мастер-пароль:", load_vault("master-pass", path))


if __name__ == "__main__":
    main()
