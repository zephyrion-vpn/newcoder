import tempfile
import threading
import time
from pathlib import Path
from typing import Optional


def watch_for_new_file(folder: Path, timeout: float = 5.0, interval: float = 0.2) -> Optional[Path]:
    before = {p.name for p in folder.iterdir()}
    deadline = time.perf_counter() + timeout
    while time.perf_counter() < deadline:
        current = {p.name for p in folder.iterdir()}
        new_names = current - before
        if new_names:
            return folder / sorted(new_names)[0]
        time.sleep(interval)
    return None


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    (tmp / "existing.txt").write_text("old", encoding="utf-8")

    def create_later() -> None:
        time.sleep(0.5)
        (tmp / "new_arrival.txt").write_text("new", encoding="utf-8")

    threading.Thread(target=create_later, daemon=True).start()

    print("Жду появления нового файла...")
    found = watch_for_new_file(tmp, timeout=3.0)
    if found:
        print(f"Обнаружен новый файл: {found.name}")
    else:
        print("Новых файлов не появилось за отведённое время.")


if __name__ == "__main__":
    main()
