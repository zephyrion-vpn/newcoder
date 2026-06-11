import os
import tempfile


def delete_empty_files(root: str) -> list[str]:
    removed = []
    for current, _dirs, files in os.walk(root):
        for name in files:
            path = os.path.join(current, name)
            if os.path.getsize(path) == 0:
                os.remove(path)
                removed.append(os.path.relpath(path, root))
    return sorted(removed)


def main() -> None:
    root = tempfile.mkdtemp()
    sub = os.path.join(root, "sub")
    os.makedirs(sub)
    open(os.path.join(root, "empty1.txt"), "w").close()
    open(os.path.join(sub, "empty2.txt"), "w").close()
    with open(os.path.join(root, "full.txt"), "w", encoding="utf-8") as handle:
        handle.write("данные")
    removed = delete_empty_files(root)
    print(f"Удалено пустых файлов: {removed}")


if __name__ == "__main__":
    main()
