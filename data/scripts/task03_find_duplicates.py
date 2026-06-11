import hashlib
import sys
from collections import defaultdict
from pathlib import Path


def file_hash(path: Path, chunk_size: int = 65536) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def find_duplicates(directory: Path) -> dict[str, list[Path]]:
    if not directory.is_dir():
        raise NotADirectoryError(f"Не является директорией: {directory}")
    by_size: dict[int, list[Path]] = defaultdict(list)
    for path in directory.rglob("*"):
        if path.is_file():
            by_size[path.stat().st_size].append(path)
    by_hash: dict[str, list[Path]] = defaultdict(list)
    for paths in by_size.values():
        if len(paths) < 2:
            continue
        for path in paths:
            by_hash[file_hash(path)].append(path)
    return {digest: paths for digest, paths in by_hash.items() if len(paths) > 1}


def main() -> None:
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    duplicates = find_duplicates(directory)
    if not duplicates:
        print("Дубликаты не найдены.")
        return
    for digest, paths in duplicates.items():
        print(f"\nХеш {digest[:12]}…")
        for path in paths:
            print(f"  {path}")


if __name__ == "__main__":
    main()
