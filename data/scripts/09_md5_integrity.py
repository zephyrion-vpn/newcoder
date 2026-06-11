import hashlib
import tempfile
from pathlib import Path

CHUNK = 65536


def md5_of_file(path: Path) -> str:
    digest = hashlib.md5()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_integrity(path: Path, expected_md5: str) -> bool:
    return md5_of_file(path) == expected_md5.lower()


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    path = tmp / "file.bin"
    path.write_text("Целостность данных важна: important data payload", encoding="utf-8")

    reference = md5_of_file(path)
    print(f"Эталонный MD5: {reference}")
    print(f"Проверка (нетронутый): {verify_integrity(path, reference)}")

    path.write_text("Целостность данных важна: important data payload!", encoding="utf-8")  # изменили
    print(f"Проверка после изменения: {verify_integrity(path, reference)}")
    print(f"Новый MD5: {md5_of_file(path)}")


if __name__ == "__main__":
    main()
