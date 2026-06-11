import os
import tempfile
from pathlib import Path


def make_unique_temp(directory: Path, prefix: str = "tmp_", suffix: str = ".dat") -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=prefix, suffix=suffix, dir=str(directory))
    os.close(fd)
    return Path(name)


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    created = [make_unique_temp(tmp) for _ in range(3)]
    print("Созданы уникальные временные файлы:")
    for path in created:
        print(f"   {path.name} (существует: {path.exists()})")
    print(f"Все имена уникальны: {len({p.name for p in created}) == len(created)}")


if __name__ == "__main__":
    main()
