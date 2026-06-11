import tempfile
from pathlib import Path


def sort_by_extension(folder: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    for entry in sorted(folder.iterdir()):
        if not entry.is_file():
            continue
        ext = entry.suffix.lstrip(".").lower() or "no_extension"
        target_dir = folder / ext
        target_dir.mkdir(exist_ok=True)
        entry.rename(target_dir / entry.name)
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def main() -> None:
    folder = Path(tempfile.mkdtemp())
    for name in ["a.jpg", "b.jpg", "c.txt", "readme"]:
        (folder / name).write_text("data", encoding="utf-8")
    counts = sort_by_extension(folder)
    print(f"Перемещено по расширениям: {counts}")
    print("jpg:", sorted(p.name for p in (folder / "jpg").iterdir()))


if __name__ == "__main__":
    main()
