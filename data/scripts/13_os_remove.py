import os
from pathlib import Path


def main() -> None:
    path = "/tmp/py_remove_demo.txt"
    Path(path).write_text("temp", encoding="utf-8")
    os.remove(path)
    print(Path(path).exists())


if __name__ == "__main__":
    main()
