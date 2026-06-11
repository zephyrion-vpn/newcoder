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
    folder = tempfile.mkdtemp()
    path = os.path.join(folder, "settings.txt")
    print(repr(safe_read(path, "настройки по умолчанию")))
    print(repr(safe_read(path, "не используется")))


if __name__ == "__main__":
    main()
