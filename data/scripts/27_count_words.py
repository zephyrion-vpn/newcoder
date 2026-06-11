from pathlib import Path


def count_words(path: str) -> int:
    with open(path, "r", encoding="utf-8") as file:
        return len(file.read().split())


def main() -> None:
    path = "/tmp/py_countwords_demo.txt"
    Path(path).write_text("one two three", encoding="utf-8")
    print(count_words(path))


if __name__ == "__main__":
    main()
