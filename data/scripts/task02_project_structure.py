import sys
from pathlib import Path

DIRECTORIES = ("src", "tests", "docs", "data")
README_NAME = "README.md"


def scaffold_project(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    for name in DIRECTORIES:
        (root / name).mkdir(exist_ok=True)
    readme = root / README_NAME
    if not readme.exists():
        readme.write_text(f"# {root.name}\n", encoding="utf-8")


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    scaffold_project(root)
    print(f"Структура проекта создана в: {root.resolve()}")


if __name__ == "__main__":
    main()
