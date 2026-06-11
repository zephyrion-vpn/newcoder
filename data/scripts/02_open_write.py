from pathlib import Path


def main() -> None:
    path = "/tmp/py_write_demo.txt"
    file = open(path, "w", encoding="utf-8")
    file.write("hello")
    file.close()
    print(Path(path).read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
