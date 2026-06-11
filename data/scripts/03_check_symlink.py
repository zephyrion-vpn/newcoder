import os
import tempfile
from pathlib import Path
from typing import Optional


def resolve_symlink(path: str) -> Optional[str]:
    p = Path(path)
    if p.is_symlink():
        target = os.readlink(path)
        print(f"{path} — символическая ссылка на: {target}")
        return target
    print(f"{path} — не символическая ссылка.")
    return None


def main() -> None:
    folder = Path(tempfile.mkdtemp())
    real = folder / "real.txt"
    real.write_text("data", encoding="utf-8")
    link = folder / "link.txt"
    try:
        os.symlink(real, link)
        resolve_symlink(str(link))
    except OSError as error:
        print(f"Не удалось создать симлинк: {error}")
    resolve_symlink(str(real))


if __name__ == "__main__":
    main()
