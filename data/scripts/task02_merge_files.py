import os
import tempfile


def merge_text_files(folder: str, output: str) -> int:
    merged = 0
    with open(output, "w", encoding="utf-8") as out:
        for name in sorted(os.listdir(folder)):
            path = os.path.join(folder, name)
            if not os.path.isfile(path):
                continue
            out.write(f"===== {name} =====\n")
            with open(path, encoding="utf-8") as handle:
                out.write(handle.read())
            out.write("\n")
            merged += 1
    return merged


def main() -> None:
    folder = tempfile.mkdtemp()
    for index in range(1, 4):
        with open(os.path.join(folder, f"part{index}.txt"), "w", encoding="utf-8") as handle:
            handle.write(f"Содержимое файла {index}")
    output = tempfile.mktemp(suffix=".txt")
    count = merge_text_files(folder, output)
    print(f"Объединено файлов: {count}")
    with open(output, encoding="utf-8") as handle:
        print(handle.read().strip())


if __name__ == "__main__":
    main()
