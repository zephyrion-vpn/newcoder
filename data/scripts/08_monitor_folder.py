import tempfile
import threading
import time
from pathlib import Path
from typing import Optional


def wait_for_new_file(folder: Path, interval: float = 0.5, max_checks: int = 10) -> Optional[Path]:
    seen = {p.name for p in folder.iterdir()}
    for _ in range(max_checks):
        time.sleep(interval)
        for entry in folder.iterdir():
            if entry.name not in seen:
                return entry
    return None


def main() -> None:
    folder = Path(tempfile.mkdtemp())
    (folder / "existing.txt").write_text("old", encoding="utf-8")

    def create_later() -> None:
        time.sleep(0.15)
        (folder / "new.txt").write_text("new", encoding="utf-8")

    worker = threading.Thread(target=create_later)
    worker.start()
    print("Ожидание нового файла...")
    found = wait_for_new_file(folder, interval=0.05, max_checks=20)
    worker.join()
    print(f"Обнаружен новый файл: {found.name if found else None}")


if __name__ == "__main__":
    main()
