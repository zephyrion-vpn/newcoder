from pathlib import Path


def find_txt_files(directory: Path) -> list[Path]:
    return sorted(directory.glob("*.txt"))


def main() -> None:
    files = find_txt_files(Path.cwd())
    if not files:
        print("Файлы .txt не найдены.")
        return
    for file in files:
        print(file.name)


if __name__ == "__main__":
    main()
