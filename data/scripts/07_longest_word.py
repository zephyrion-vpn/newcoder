import glob
import os
import re
import tempfile

WORD_PATTERN = re.compile(r"\w+", re.UNICODE)


def longest_word_in_folder(folder: str) -> str | None:
    longest = ""
    for path in sorted(glob.glob(os.path.join(folder, "*.txt"))):
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                for match in WORD_PATTERN.finditer(line):
                    word = match.group()
                    if len(word) > len(longest):
                        longest = word
    return longest or None


def main() -> None:
    folder = tempfile.mkdtemp()
    with open(os.path.join(folder, "a.txt"), "w", encoding="utf-8") as handle:
        handle.write("короткое слово")
    with open(os.path.join(folder, "b.txt"), "w", encoding="utf-8") as handle:
        handle.write("непревзойдённый результат")
    print(f"Самое длинное слово: {longest_word_in_folder(folder)}")


if __name__ == "__main__":
    main()
