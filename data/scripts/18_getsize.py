import os
from pathlib import Path


def main() -> None:
    path = "/tmp/py_size_demo.txt"
    Path(path).write_text("hello", encoding="utf-8")
    print(os.path.getsize(path))


if __name__ == "__main__":
    main()
