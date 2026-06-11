import shutil
from pathlib import Path


def main() -> None:
    source = "/tmp/py_copy_src.txt"
    target = "/tmp/py_copy_dst.txt"
    Path(source).write_text("data", encoding="utf-8")
    shutil.copy(source, target)
    print(Path(target).read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
