import os
import tempfile


def dump_env(path: str) -> int:
    with open(path, "w", encoding="utf-8") as handle:
        for key, value in sorted(os.environ.items()):
            handle.write(f"{key}={value}\n")
    return len(os.environ)


def main() -> None:
    path = tempfile.mktemp(suffix=".env")
    count = dump_env(path)
    print(f"Сохранено переменных: {count}")
    with open(path, encoding="utf-8") as handle:
        preview = handle.readlines()[:3]
    print("Первые строки:")
    for line in preview:
        print(" ", line.strip())
    os.remove(path)


if __name__ == "__main__":
    main()
