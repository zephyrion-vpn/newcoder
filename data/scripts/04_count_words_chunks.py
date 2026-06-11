import os
import tempfile
from typing import Iterator


def read_chunks(path: str, chunk_size: int = 65536) -> Iterator[str]:
    with open(path, encoding="utf-8") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                return
            yield chunk


def count_words(path: str, chunk_size: int = 65536) -> int:
    total = 0
    trailing_non_space = False
    for chunk in read_chunks(path, chunk_size):
        words = chunk.split()
        if not words:
            if chunk and not chunk[0].isspace():
                pass
            trailing_non_space = trailing_non_space and not chunk[:1].isspace()
            continue
        total += len(words)
        if trailing_non_space and not chunk[0].isspace():
            total -= 1
        trailing_non_space = not chunk[-1].isspace()
    return total


def main() -> None:
    path = os.path.join(tempfile.mkdtemp(), "big.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("слово " * 1000)
    print(f"Всего слов: {count_words(path, chunk_size=64)}")


if __name__ == "__main__":
    main()
