import os
from pathlib import Path


def main() -> None:
    directory = "/tmp/py_listdir_demo"
    os.makedirs(directory, exist_ok=True)
    Path(directory, "a.txt").write_text("a", encoding="utf-8")
    print(os.listdir(directory))


if __name__ == "__main__":
    main()
