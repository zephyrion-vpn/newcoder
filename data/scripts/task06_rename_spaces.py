import sys
from pathlib import Path


def rename_spaces_to_underscores(directory: Path) -> list[tuple[Path, Path]]:
    if not directory.is_dir():
        raise NotADirectoryError(f"Не является директорией: {directory}")
    renamed: list[tuple[Path, Path]] = []
    for path in directory.iterdir():
        if not path.is_file() or " " not in path.name:
            continue
        target = path.with_name(path.name.replace(" ", "_"))
        if target.exists():
            print(f"Пропуск: {target.name} уже существует", file=sys.stderr)
            continue
        path.rename(target)
        renamed.append((path, target))
    return renamed


def main() -> None:
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    for source, target in rename_spaces_to_underscores(directory):
        print(f"{source.name} -> {target.name}")


if __name__ == "__main__":
    main()
