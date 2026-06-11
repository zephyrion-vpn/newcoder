import os
import tempfile


def count_words(path: str, chunk_size: int = 1 << 20) -> int:
    count = 0
    leftover = ""
    with open(path, encoding="utf-8") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            combined = leftover + chunk
            if combined[-1].isspace():
                count += len(combined.split())
                leftover = ""
            else:
                parts = combined.split()
                leftover = parts.pop() if parts else ""
                count += len(parts)
    if leftover.strip():
        count += 1
    return count


def main() -> None:
    path = tempfile.mktemp(suffix=".txt")
    with open(path, "w", encoding="utf-8") as handle:
        for _ in range(10_000):
            handle.write("один два три четыре пять ")
    print("Слов в файле:", count_words(path, chunk_size=4096))
    os.remove(path)


if __name__ == "__main__":
    main()
