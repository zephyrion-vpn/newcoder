import glob
import os
import tempfile
import zipfile


def archive_logs(folder: str, archive_path: str) -> int:
    log_files = sorted(glob.glob(os.path.join(folder, "*.log")))
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in log_files:
            archive.write(path, arcname=os.path.basename(path))
    return len(log_files)


def main() -> None:
    folder = tempfile.mkdtemp()
    for name in ["app.log", "error.log", "notes.txt"]:
        with open(os.path.join(folder, name), "w", encoding="utf-8") as handle:
            handle.write(f"содержимое {name}")
    archive_path = os.path.join(folder, "logs.zip")
    count = archive_logs(folder, archive_path)
    print(f"Заархивировано файлов: {count}")
    with zipfile.ZipFile(archive_path) as archive:
        print(archive.namelist())


if __name__ == "__main__":
    main()
