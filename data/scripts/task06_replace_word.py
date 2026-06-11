import os
import tempfile


def replace_word(folder: str, old: str, new: str) -> list[str]:
    changed: list[str] = []
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".txt"):
            continue
        path = os.path.join(folder, name)
        with open(path, encoding="utf-8") as handle:
            content = handle.read()
        if old in content:
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(content.replace(old, new))
            changed.append(name)
    return changed


def main() -> None:
    folder = tempfile.mkdtemp()
    with open(os.path.join(folder, "a.txt"), "w", encoding="utf-8") as handle:
        handle.write("кошка и ещё кошка")
    with open(os.path.join(folder, "b.txt"), "w", encoding="utf-8") as handle:
        handle.write("здесь нет слова")
    changed = replace_word(folder, old="кошка", new="собака")
    print("Изменены файлы:", changed)
    with open(os.path.join(folder, "a.txt"), encoding="utf-8") as handle:
        print("a.txt:", handle.read())


if __name__ == "__main__":
    main()
