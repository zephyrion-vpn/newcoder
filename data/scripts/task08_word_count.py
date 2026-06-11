import re
import sys
from pathlib import Path


def count_word_occurrences(path: Path, word: str) -> int:
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)
    return len(pattern.findall(text))


def main() -> None:
    if len(sys.argv) != 3:
        print(f"Использование: {Path(sys.argv[0]).name} <файл> <слово>", file=sys.stderr)
        raise SystemExit(2)
    path = Path(sys.argv[1])
    word = sys.argv[2]
    if not path.is_file():
        print(f"Файл не найден: {path}", file=sys.stderr)
        raise SystemExit(1)
    print(count_word_occurrences(path, word))


if __name__ == "__main__":
    main()
