from pathlib import Path


def main() -> None:
    path = "/tmp/py_append_demo.txt"
    Path(path).write_text("line1\n", encoding="utf-8")
    file = open(path, "a", encoding="utf-8")
    file.write("line2\n")
    file.close()
    print(Path(path).read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
