import tempfile
from pathlib import Path


def rename_spaces(folder: str) -> list[tuple[str, str]]:
    renamed: list[tuple[str, str]] = []
    for path in Path(folder).iterdir():
        if path.is_file() and " " in path.name:
            target = path.with_name(path.name.replace(" ", "_"))
            path.rename(target)
            renamed.append((path.name, target.name))
    return renamed


def main() -> None:
    folder = Path(tempfile.mkdtemp())
    for name in ("my file.txt", "report final.csv", "ok.txt"):
        (folder / name).write_text("x", encoding="utf-8")
    for old, new in rename_spaces(str(folder)):
        print(f"{old!r} -> {new!r}")
    print("Итого в папке:", sorted(p.name for p in folder.iterdir()))


if __name__ == "__main__":
    main()
