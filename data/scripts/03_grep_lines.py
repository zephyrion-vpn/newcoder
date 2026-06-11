import os
import tempfile
from typing import Iterator


def lines_with_word(path: str, word: str) -> Iterator[str]:
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if word in line:
                yield line.rstrip("\n")


def main() -> None:
    path = os.path.join(tempfile.gettempdir(), "grep_demo.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("первая строка python\n")
        handle.write("вторая строка\n")
        handle.write("третья python строка\n")
    for line in lines_with_word(path, "python"):
        print(line)


if __name__ == "__main__":
    main()
