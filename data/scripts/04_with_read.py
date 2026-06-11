from pathlib import Path


def main() -> None:
    path = "/tmp/py_with_demo.txt"
    Path(path).write_text("hello", encoding="utf-8")
    with open(path, "r", encoding="utf-8") as file:
        print(file.read())


if __name__ == "__main__":
    main()
