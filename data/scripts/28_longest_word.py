from pathlib import Path


def longest_word(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return max(file.read().split(), key=len)


def main() -> None:
    path = "/tmp/py_longest_demo.txt"
    Path(path).write_text("a bb ccc dd", encoding="utf-8")
    print(longest_word(path))


if __name__ == "__main__":
    main()
