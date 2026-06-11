import glob
import os
import tempfile


def replace_word_in_folder(folder: str, old: str, new: str) -> int:
    changed = 0
    for path in sorted(glob.glob(os.path.join(folder, "*.txt"))):
        with open(path, encoding="utf-8") as handle:
            content = handle.read()
        if old in content:
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(content.replace(old, new))
            changed += 1
    return changed


def main() -> None:
    folder = tempfile.mkdtemp()
    for name, text in [("a.txt", "кот и кот"), ("b.txt", "собака")]:
        with open(os.path.join(folder, name), "w", encoding="utf-8") as handle:
            handle.write(text)
    changed = replace_word_in_folder(folder, "кот", "пёс")
    print(f"Изменено файлов: {changed}")
    with open(os.path.join(folder, "a.txt"), encoding="utf-8") as handle:
        print(handle.read())


if __name__ == "__main__":
    main()
