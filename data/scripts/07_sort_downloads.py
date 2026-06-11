import tempfile
from pathlib import Path

CATEGORIES = {
    "Документы": {".pdf", ".doc", ".docx", ".txt"},
    "Картинки": {".jpg", ".jpeg", ".png", ".gif"},
    "Установщики": {".exe", ".msi", ".dmg"},
}


def sort_downloads(folder: Path) -> dict[str, list[str]]:
    moved: dict[str, list[str]] = {}
    ext_to_category = {ext: cat for cat, exts in CATEGORIES.items() for ext in exts}
    for entry in sorted(folder.iterdir()):
        if not entry.is_file():
            continue
        category = ext_to_category.get(entry.suffix.lower())
        if category is None:
            continue
        target_dir = folder / category
        target_dir.mkdir(exist_ok=True)
        entry.rename(target_dir / entry.name)
        moved.setdefault(category, []).append(entry.name)
    return moved


def main() -> None:
    folder = Path(tempfile.mkdtemp())
    for name in ["report.pdf", "photo.jpg", "setup.exe", "notes.txt", "unknown.xyz"]:
        (folder / name).write_text("data", encoding="utf-8")
    moved = sort_downloads(folder)
    for category, names in moved.items():
        print(f"{category}: {names}")


if __name__ == "__main__":
    main()
