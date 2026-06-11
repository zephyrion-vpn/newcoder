import os
from pathlib import Path


def main() -> None:
    path = "/tmp/py_isfile_demo.txt"
    Path(path).write_text("x", encoding="utf-8")
    print(os.path.isfile(path))


if __name__ == "__main__":
    main()
