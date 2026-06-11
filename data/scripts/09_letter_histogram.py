import tempfile
from collections import Counter
from pathlib import Path


def letter_frequencies(text: str) -> Counter:
    return Counter(ch for ch in text.lower() if ch.isalpha())


def render_histogram(frequencies: Counter, bar_char: str = "█", width: int = 40) -> str:
    if not frequencies:
        return "(нет букв)"
    max_count = max(frequencies.values())
    lines: list[str] = []
    for letter, count in sorted(frequencies.items(), key=lambda kv: (-kv[1], kv[0])):
        bar_len = round(count / max_count * width)
        lines.append(f"{letter} | {bar_char * bar_len} {count}")
    return "\n".join(lines)


def main() -> None:
    path = Path(tempfile.mkdtemp()) / "sample.txt"
    path.write_text("Мама мыла раму. Hello, hello!", encoding="utf-8")
    text = path.read_text(encoding="utf-8")
    print(render_histogram(letter_frequencies(text)))


if __name__ == "__main__":
    main()
