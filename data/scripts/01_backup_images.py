import os
import shutil
import tempfile

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}


def backup_images(source: str, backup_name: str = "images_backup") -> int:
    backup_dir = os.path.join(source, backup_name)
    os.makedirs(backup_dir, exist_ok=True)
    copied = 0
    for name in sorted(os.listdir(source)):
        path = os.path.join(source, name)
        if not os.path.isfile(path):
            continue
        if os.path.splitext(name)[1].lower() in IMAGE_EXTENSIONS:
            shutil.copy2(path, os.path.join(backup_dir, name))
            copied += 1
    return copied


def main() -> None:
    folder = tempfile.mkdtemp()
    for name in ["a.jpg", "b.png", "c.txt", "d.JPG"]:
        with open(os.path.join(folder, name), "w", encoding="utf-8") as handle:
            handle.write("data")
    copied = backup_images(folder)
    print(f"Скопировано изображений: {copied}")
    print(sorted(os.listdir(os.path.join(folder, "images_backup"))))


if __name__ == "__main__":
    main()
