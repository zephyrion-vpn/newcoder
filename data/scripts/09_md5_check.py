import hashlib
import os
import tempfile


def md5_of_file(path: str, chunk_size: int = 65536) -> str:
    digest = hashlib.md5()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_file(path: str, expected: str) -> bool:
    return md5_of_file(path) == expected.lower()


def main() -> None:
    path = os.path.join(tempfile.mkdtemp(), "data.bin")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("контрольные данные")
    actual = md5_of_file(path)
    print(f"MD5: {actual}")
    print(f"Целостность OK: {verify_file(path, actual)}")
    print(f"С неверным хешем: {verify_file(path, '0' * 32)}")


if __name__ == "__main__":
    main()
