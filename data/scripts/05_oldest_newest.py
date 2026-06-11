import os
import tempfile
import time
from pathlib import Path
from typing import Optional


def oldest_and_newest(folder: Path) -> tuple[Optional[Path], Optional[Path]]:
    files = [p for p in folder.iterdir() if p.is_file()]
    if not files:
        return None, None
    oldest = min(files, key=lambda p: p.stat().st_mtime)
    newest = max(files, key=lambda p: p.stat().st_mtime)
    return oldest, newest


def main() -> None:
    folder = Path(tempfile.mkdtemp())
    for name in ["first.txt", "second.txt", "third.txt"]:
        (folder / name).write_text("data", encoding="utf-8")
        time.sleep(0.01)
    oldest, newest = oldest_and_newest(folder)
    print(f"Самый старый: {oldest.name if oldest else None}")
    print(f"Самый новый: {newest.name if newest else None}")


if __name__ == "__main__":
    main()
