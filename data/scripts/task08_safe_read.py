import os
import tempfile


def safe_read(path: str, default: str = "") -> str:
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(default)
        return default
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def main() -> None:
    path = tempfile.mktemp(suffix=".txt")
    print("Файл существует:", os.path.exists(path))
    first = safe_read(path, default="значение по умолчанию")
    print("Первое чтение (создан):", first)
    second = safe_read(path, default="другое")
    print("Второе чтение (существует):", second)
    os.remove(path)


if __name__ == "__main__":
    main()
