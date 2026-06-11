import os
import tempfile
from itertools import zip_longest


def diff_lines(path_a: str, path_b: str) -> list[int]:
    with open(path_a, encoding="utf-8") as handle:
        lines_a = handle.read().splitlines()
    with open(path_b, encoding="utf-8") as handle:
        lines_b = handle.read().splitlines()
    differing = []
    for number, (a, b) in enumerate(zip_longest(lines_a, lines_b), start=1):
        if a != b:
            differing.append(number)
    return differing


def main() -> None:
    folder = tempfile.mkdtemp()
    path_a = os.path.join(folder, "a.txt")
    path_b = os.path.join(folder, "b.txt")
    with open(path_a, "w", encoding="utf-8") as handle:
        handle.write("строка 1\nстрока 2\nстрока 3\n")
    with open(path_b, "w", encoding="utf-8") as handle:
        handle.write("строка 1\nИЗМЕНЕНО\nстрока 3\nстрока 4\n")
    print(f"Отличающиеся строки: {diff_lines(path_a, path_b)}")


if __name__ == "__main__":
    main()
