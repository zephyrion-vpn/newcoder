import shutil
import tempfile
from pathlib import Path


def organize_by_extension(folder: Path) -> dict[str, int]:
    if not folder.is_dir():
        raise NotADirectoryError(f"Не папка: {folder}")
    moved: dict[str, int] = {}
    for path in list(folder.iterdir()):
        if not path.is_file():
            continue
        ext = path.suffix.lower().lstrip(".")
        if not ext:
            ext = "no_extension"
        target_dir = folder / ext
        target_dir.mkdir(exist_ok=True)
        target = target_dir / path.name
        counter = 1
        while target.exists():
            target = target_dir / f"{path.stem}_{counter}{path.suffix}"
            counter += 1
        shutil.move(str(path), str(target))
        moved[ext] = moved.get(ext, 0) + 1
    return moved


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    for name in ("a.jpg", "b.jpg", "c.png", "notes.txt", "data.csv", "README"):
        (tmp / name).write_text("x", encoding="utf-8")

    moved = organize_by_extension(tmp)
    print("Перемещено по расширениям:", moved)
    print("Структура после:")
    for path in sorted(tmp.rglob("*")):
        print(f"   {path.relative_to(tmp)}")


if __name__ == "__main__":
    main()
