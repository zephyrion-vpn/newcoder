import os
import tempfile


def process_files(paths: list[str]) -> tuple[list[str], list[str]]:
    contents: list[str] = []
    failed_files: list[str] = []
    for path in paths:
        try:
            with open(path, encoding="utf-8") as handle:
                contents.append(handle.read())
        except OSError:
            failed_files.append(path)
    return contents, failed_files


def main() -> None:
    folder = tempfile.mkdtemp()
    good = os.path.join(folder, "good.txt")
    with open(good, "w", encoding="utf-8") as handle:
        handle.write("данные")
    missing = os.path.join(folder, "missing.txt")
    contents, failed = process_files([good, missing])
    print(f"Прочитано файлов: {len(contents)}")
    print(f"Не удалось: {[os.path.basename(p) for p in failed]}")


if __name__ == "__main__":
    main()
