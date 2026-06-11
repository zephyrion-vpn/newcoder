from pathlib import Path


def main() -> None:
    path = Path("/tmp/py_readtext_demo.txt")
    path.write_text("hello", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
