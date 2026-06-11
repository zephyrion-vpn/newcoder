import tempfile
from pathlib import Path


def create_project(root: str) -> Path:
    base = Path(root)
    for folder in ("src", "tests", "docs", "data"):
        (base / folder).mkdir(parents=True, exist_ok=True)
    readme = base / "README.md"
    readme.write_text(f"# {base.name}\n\nОписание проекта.\n", encoding="utf-8")
    return base


def main() -> None:
    root = Path(tempfile.mkdtemp()) / "my_project"
    base = create_project(str(root))
    for item in sorted(base.iterdir()):
        marker = "/" if item.is_dir() else ""
        print(f"{item.name}{marker}")


if __name__ == "__main__":
    main()
