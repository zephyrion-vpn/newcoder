import base64
import getpass
import json
import os
import sys
import tempfile

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def _derive_key(master: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=200_000)
    return base64.urlsafe_b64encode(kdf.derive(master.encode("utf-8")))


def save_vault(path: str, master: str, data: dict[str, str]) -> None:
    salt = os.urandom(16)
    token = Fernet(_derive_key(master, salt)).encrypt(json.dumps(data).encode("utf-8"))
    with open(path, "wb") as handle:
        handle.write(salt + token)


def load_vault(path: str, master: str) -> dict[str, str]:
    with open(path, "rb") as handle:
        blob = handle.read()
    salt, token = blob[:16], blob[16:]
    try:
        plaintext = Fernet(_derive_key(master, salt)).decrypt(token)
    except InvalidToken as error:
        raise ValueError("Неверный мастер-пароль") from error
    return json.loads(plaintext.decode("utf-8"))


def main() -> None:
    path = tempfile.mktemp(suffix=".vault")
    if sys.stdin.isatty():
        master = getpass.getpass("Мастер-пароль: ")
    else:
        master = "demo-master"
        print("[демо] используется мастер-пароль 'demo-master'")
    save_vault(path, master, {"github.com": "p@ss1", "mail.ru": "secret2"})
    print("Хранилище зашифровано и сохранено")
    print("Расшифровано:", load_vault(path, master))
    try:
        load_vault(path, "wrong-password")
    except ValueError as error:
        print("Попытка с неверным паролем:", error)
    os.remove(path)


if __name__ == "__main__":
    main()
