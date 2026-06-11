import sys
from datetime import datetime, timedelta
from pathlib import Path


def find_recent_files(directory: Path, within: timedelta = timedelta(hours=24)) -> list[Path]:
    if not directory.is_dir():
        raise NotADirectoryError(f"Не является директорией: {directory}")
    threshold = (datetime.now() - within).timestamp()
    return sorted(
        path
        for path in directory.rglob("*")
        if path.is_file() and path.stat().st_ctime >= threshold
    )


def main() -> None:
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    for path in find_recent_files(directory):
        print(path)


if __name__ == "__main__":
    main()
