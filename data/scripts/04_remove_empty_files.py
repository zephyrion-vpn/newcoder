import tempfile
from pathlib import Path


def remove_empty_files(root: Path) -> list[Path]:
    if not root.is_dir():
        raise NotADirectoryError(f"Не папка: {root}")
    removed: list[Path] = []
    for path in root.rglob("*"):
        if path.is_file() and path.stat().st_size == 0:
            removed.append(path.relative_to(root))
            path.unlink()
    return removed


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    (tmp / "sub").mkdir()
    (tmp / "empty1.txt").write_bytes(b"")
    (tmp / "data.txt").write_text("есть данные", encoding="utf-8")
    (tmp / "sub" / "empty2.log").write_bytes(b"")
    (tmp / "sub" / "keep.bin").write_bytes(b"\x00\x01")

    removed = remove_empty_files(tmp)
    print(f"Удалено пустых файлов: {len(removed)}")
    for path in sorted(map(str, removed)):
        print(f"   {path}")
    remaining = sorted(str(p.relative_to(tmp)) for p in tmp.rglob("*") if p.is_file())
    print("Остались:", remaining)


if __name__ == "__main__":
    main()
