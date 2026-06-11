import tempfile
from pathlib import Path


def folder_size_mb(folder: str) -> float:
    total = sum(
        path.stat().st_size for path in Path(folder).rglob("*") if path.is_file()
    )
    return total / 1024 / 1024


def main() -> None:
    folder = Path(tempfile.mkdtemp())
    (folder / "a.bin").write_bytes(b"x" * (2 * 1024 * 1024))
    (folder / "sub").mkdir()
    (folder / "sub" / "b.bin").write_bytes(b"y" * (1024 * 1024))
    print(f"Размер папки: {folder_size_mb(str(folder)):.2f} МБ")


if __name__ == "__main__":
    main()
