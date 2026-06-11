from pathlib import Path


def main() -> None:
    path = "/tmp/py_writestring_demo.txt"
    with open(path, "w", encoding="utf-8") as file:
        file.write("hello")
    print(Path(path).read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
