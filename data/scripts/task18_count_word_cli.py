import os
import re
import sys
import tempfile


def count_word(path: str, word: str) -> int:
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    tokens = re.findall(r"\w+", text.lower(), flags=re.UNICODE)
    return tokens.count(word.lower())


def main() -> None:
    if len(sys.argv) == 3:
        path, word = sys.argv[1], sys.argv[2]
        cleanup = False
    else:
        print("Демо-режим (использование: python task18_count_word_cli.py <файл> <слово>)")
        path = tempfile.mktemp(suffix=".txt")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write("кот и пёс и снова кот, а вот ещё кот")
        word = "кот"
        cleanup = True
    try:
        count = count_word(path, word)
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        sys.exit(1)
    print(f"Слово {word!r} встречается {count} раз(а)")
    if cleanup:
        os.remove(path)


if __name__ == "__main__":
    main()
