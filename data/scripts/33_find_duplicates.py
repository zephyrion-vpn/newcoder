import hashlib
import tempfile
from collections import defaultdict
from pathlib import Path

CHUNK = 65536


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()


def find_duplicates(folder: Path) -> dict[str, list[Path]]:
    by_hash: dict[str, list[Path]] = defaultdict(list)
    for path in folder.rglob("*"):
        if path.is_file():
            by_hash[file_hash(path)].append(path)
    return {h: paths for h, paths in by_hash.items() if len(paths) > 1}


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    (tmp / "a.txt").write_text("одинаковое содержимое", encoding="utf-8")
    (tmp / "sub").mkdir()
    (tmp / "sub" / "b_copy.txt").write_text("одинаковое содержимое", encoding="utf-8")
    (tmp / "unique.txt").write_text("уникальное", encoding="utf-8")
    (tmp / "c_copy.txt").write_text("одинаковое содержимое", encoding="utf-8")

    duplicates = find_duplicates(tmp)
    if not duplicates:
        print("Дубликатов не найдено.")
        return
    print(f"Найдено групп дубликатов: {len(duplicates)}")
    for digest, paths in duplicates.items():
        print(f"Хеш {digest[:12]}... ({len(paths)} файла):")
        for path in sorted(paths):
            print(f"   {path.relative_to(tmp)}")


if __name__ == "__main__":
    main()
