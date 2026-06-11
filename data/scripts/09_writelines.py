from pathlib import Path


def main() -> None:
    path = "/tmp/py_writelines_demo.txt"
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(["a\n", "b\n"])
    print(Path(path).read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
