import os
import tempfile
import zipfile


def archive_logs(directory: str, archive_path: str) -> list[str]:
    logs = [
        name
        for name in sorted(os.listdir(directory))
        if name.endswith(".log") and os.path.isfile(os.path.join(directory, name))
    ]
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in logs:
            archive.write(os.path.join(directory, name), arcname=name)
    return logs


def main() -> None:
    directory = tempfile.mkdtemp()
    for name in ("app.log", "error.log", "notes.txt"):
        with open(os.path.join(directory, name), "w", encoding="utf-8") as handle:
            handle.write("demo")
    archive_path = tempfile.mktemp(suffix=".zip")
    archived = archive_logs(directory, archive_path)
    print("Заархивировано:", archived)
    with zipfile.ZipFile(archive_path) as archive:
        print("В архиве:", archive.namelist())
    os.remove(archive_path)


if __name__ == "__main__":
    main()
