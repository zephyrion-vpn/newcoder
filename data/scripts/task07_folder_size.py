import sys
from pathlib import Path


def folder_size_mb(directory: Path) -> float:
    if not directory.is_dir():
        raise NotADirectoryError(f"Не является директорией: {directory}")
    total = 0
    for path in directory.rglob("*"):
        if path.is_file():
            try:
                total += path.stat().st_size
            except OSError:
                continue
    return total / (1024 * 1024)


def main() -> None:
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    print(f"{folder_size_mb(directory):.2f} МБ")


if __name__ == "__main__":
    main()
