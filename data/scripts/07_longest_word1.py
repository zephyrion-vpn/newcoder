import re
import tempfile
from pathlib import Path


def find_longest_word(folder: Path) -> tuple[str, Path | None]:
    longest = ""
    source: Path | None = None
    for path in folder.rglob("*.txt"):
        if not path.is_file():
            continue
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            for line in handle:
                for word in re.findall(r"\w+", line, re.UNICODE):
                    if len(word) > len(longest):
                        longest = word
                        source = path
    return longest, source


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    (tmp / "sub").mkdir()
    (tmp / "a.txt").write_text("короткие слова тут", encoding="utf-8")
    (tmp / "sub" / "b.txt").write_text("суперкалифраджилистикекспиалидоциюс и обычные", encoding="utf-8")
    (tmp / "ignore.md").write_text("этотфайлнеучитываетсяоченьдлинное", encoding="utf-8")

    word, source = find_longest_word(tmp)
    print(f"Самое длинное слово: {word!r} ({len(word)} симв.)")
    print(f"Найдено в: {source.name if source else '—'}")


if __name__ == "__main__":
    main()
