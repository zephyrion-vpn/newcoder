import shutil
import tempfile
from pathlib import Path

MAPPING = {
    ".pdf": "Документы",
    ".jpg": "Картинки",
    ".jpeg": "Картинки",
    ".exe": "Установщики",
}


def sort_downloads(folder: str) -> dict[str, str]:
    base = Path(folder)
    moved: dict[str, str] = {}
    for path in list(base.iterdir()):
        if not path.is_file():
            continue
        category = MAPPING.get(path.suffix.lower())
        if category is None:
            continue
        destination = base / category
        destination.mkdir(exist_ok=True)
        shutil.move(str(path), str(destination / path.name))
        moved[path.name] = category
    return moved


def main() -> None:
    folder = Path(tempfile.mkdtemp())
    for name in ("resume.pdf", "photo.jpg", "setup.exe", "notes.txt"):
        (folder / name).write_text("x", encoding="utf-8")
    moved = sort_downloads(str(folder))
    for name, category in moved.items():
        print(f"{name} -> {category}/")
    print("Осталось в корне:", sorted(p.name for p in folder.iterdir() if p.is_file()))


if __name__ == "__main__":
    main()
