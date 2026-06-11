import os
from pathlib import Path


def export_environment(path: Path) -> int:
    items = sorted(os.environ.items())
    path.write_text("".join(f"{key}={value}\n" for key, value in items), encoding="utf-8")
    return len(items)


def main() -> None:
    path = Path(".env")
    count = export_environment(path)
    print(f"Сохранено {count} переменных в {path.resolve()}")


if __name__ == "__main__":
    main()
