from pathlib import Path


def main() -> None:
    path = "/tmp/py_iterate_demo.txt"
    Path(path).write_text("a\nb\nc\n", encoding="utf-8")
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())


if __name__ == "__main__":
    main()
