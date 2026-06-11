import os
import tempfile


def merge_text_files(folder: str, destination: str) -> int:
    names = sorted(name for name in os.listdir(folder) if name.endswith(".txt"))
    with open(destination, "w", encoding="utf-8") as outfile:
        for name in names:
            path = os.path.join(folder, name)
            with open(path, encoding="utf-8") as infile:
                outfile.write(f"===== {name} =====\n")
                outfile.write(infile.read().rstrip("\n") + "\n\n")
    return len(names)


def main() -> None:
    folder = tempfile.mkdtemp()
    for name, text in [("a.txt", "Содержимое A"), ("b.txt", "Содержимое B")]:
        with open(os.path.join(folder, name), "w", encoding="utf-8") as handle:
            handle.write(text)
    destination = os.path.join(folder, "merged.out")
    count = merge_text_files(folder, destination)
    print(f"Объединено файлов: {count}")
    with open(destination, encoding="utf-8") as handle:
        print(handle.read().strip())


if __name__ == "__main__":
    main()
