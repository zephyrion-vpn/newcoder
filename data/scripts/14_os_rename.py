import os
from pathlib import Path


def main() -> None:
    source = "/tmp/py_rename_src.txt"
    target = "/tmp/py_rename_dst.txt"
    Path(source).write_text("data", encoding="utf-8")
    if Path(target).exists():
        os.remove(target)
    os.rename(source, target)
    print(Path(target).exists())


if __name__ == "__main__":
    main()
