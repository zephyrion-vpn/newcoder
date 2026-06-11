import os
import tempfile
from collections import Counter


def build_histogram(path: str, bar_char: str = "\u2588", width: int = 40) -> None:
    with open(path, encoding="utf-8") as handle:
        text = handle.read().lower()
    counts = Counter(char for char in text if char.isalpha())
    if not counts:
        print("Букв не найдено")
        return
    peak = max(counts.values())
    for letter, count in sorted(counts.items()):
        length = max(1, round(count / peak * width))
        print(f"{letter}: {bar_char * length} {count}")


def main() -> None:
    path = tempfile.mktemp(suffix=".txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("the quick brown fox jumps over the lazy dog " * 5)
    build_histogram(path)
    os.remove(path)


if __name__ == "__main__":
    main()
