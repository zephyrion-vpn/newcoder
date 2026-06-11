from pathlib import Path


def main() -> None:
    path = Path("/tmp/py_read_demo.txt")
    path.write_text("hello\nworld\n", encoding="utf-8")
    file = open(path, "r", encoding="utf-8")
    print(file.read())
    file.close()


if __name__ == "__main__":
    main()
