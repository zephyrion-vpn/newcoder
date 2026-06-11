import tempfile
import time
from pathlib import Path


def find_oldest_newest(folder: Path) -> tuple[Path | None, Path | None]:
    files = [p for p in folder.rglob("*") if p.is_file()]
    if not files:
        return None, None
    oldest = min(files, key=lambda p: p.stat().st_mtime)
    newest = max(files, key=lambda p: p.stat().st_mtime)
    return oldest, newest


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    for i in range(3):
        path = tmp / f"file_{i}.txt"
        path.write_text(str(i), encoding="utf-8")
        time.sleep(0.05)

    oldest, newest = find_oldest_newest(tmp)
    print(f"Самый старый: {oldest.name if oldest else '—'}")
    print(f"Самый новый: {newest.name if newest else '—'}")
    if oldest and newest:
        delta = newest.stat().st_mtime - oldest.stat().st_mtime
        print(f"Разница во времени: {delta:.3f} с")


if __name__ == "__main__":
    main()
