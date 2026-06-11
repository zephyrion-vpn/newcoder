from pathlib import Path


def count_lines(path: str) -> int:
    with open(path, "r", encoding="utf-8") as file:
        return sum(1 for _ in file)


def main() -> None:
    path = "/tmp/py_countlines_demo.txt"
    Path(path).write_text("a\nb\nc\n", encoding="utf-8")
    print(count_lines(path))


if __name__ == "__main__":
    main()
