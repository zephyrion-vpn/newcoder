import hashlib
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path


def hash_file(path: str, algorithm: str = "sha256", chunk_size: int = 1 << 20) -> tuple[str, str]:
    digest = hashlib.new(algorithm)
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return path, digest.hexdigest()


def hash_files(paths: list[str], algorithm: str = "sha256") -> dict[str, str]:
    with ProcessPoolExecutor() as executor:
        results = executor.map(hash_file, paths, [algorithm] * len(paths))
        return dict(results)


def main() -> None:
    paths = sys.argv[1:]
    if not paths:
        print(f"Использование: {Path(sys.argv[0]).name} <файл> [файл ...]", file=sys.stderr)
        raise SystemExit(2)
    missing = [path for path in paths if not Path(path).is_file()]
    if missing:
        print(f"Не найдены файлы: {missing}", file=sys.stderr)
        raise SystemExit(1)
    for path, digest in hash_files(paths).items():
        print(f"{digest}  {path}")


if __name__ == "__main__":
    main()
