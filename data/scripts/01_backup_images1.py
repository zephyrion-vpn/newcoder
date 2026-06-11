import shutil
import tempfile
from pathlib import Path

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def backup_images(source: Path, backup_name: str = "images_backup") -> int:
    if not source.is_dir():
        raise NotADirectoryError(f"Не папка: {source}")
    destination = source / backup_name
    destination.mkdir(exist_ok=True)
    copied = 0
    for path in source.rglob("*"):
        if destination in path.parents:
            continue
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
            target = destination / path.name
            stem, suffix = target.stem, target.suffix
            counter = 1
            while target.exists():
                target = destination / f"{stem}_{counter}{suffix}"
                counter += 1
            shutil.copy2(path, target)
            copied += 1
    return copied


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    (tmp / "sub").mkdir()
    for name in ("a.jpg", "b.png", "c.txt", "sub/d.jpeg", "sub/e.PNG", "sub/f.doc"):
        file_path = tmp / name
        file_path.write_bytes(b"data")

    count = backup_images(tmp)
    backup = tmp / "images_backup"
    print(f"Скопировано изображений: {count}")
    print("Содержимое images_backup:", sorted(p.name for p in backup.iterdir()))


if __name__ == "__main__":
    main()
