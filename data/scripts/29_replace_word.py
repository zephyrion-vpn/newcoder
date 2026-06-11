from pathlib import Path


def replace_word(source: str, target: str, old: str, new: str) -> None:
    text = Path(source).read_text(encoding="utf-8")
    Path(target).write_text(text.replace(old, new), encoding="utf-8")


def main() -> None:
    source = "/tmp/py_replace_src.txt"
    target = "/tmp/py_replace_dst.txt"
    Path(source).write_text("hello world", encoding="utf-8")
    replace_word(source, target, "world", "python")
    print(Path(target).read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
