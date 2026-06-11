import tempfile
from datetime import datetime, timedelta
from pathlib import Path


def recent_files(directory: str, hours: int = 24) -> list[Path]:
    cutoff = (datetime.now() - timedelta(hours=hours)).timestamp()
    found: list[Path] = []
    for path in Path(directory).rglob("*"):
        if path.is_file() and path.stat().st_mtime >= cutoff:
            found.append(path)
    return found


def main() -> None:
    root = Path(tempfile.mkdtemp())
    (root / "sub").mkdir()
    (root / "fresh.txt").write_text("new", encoding="utf-8")
    (root / "sub" / "nested.txt").write_text("new", encoding="utf-8")
    for path in recent_files(str(root)):
        print("Свежий файл:", path.relative_to(root))


if __name__ == "__main__":
    main()
