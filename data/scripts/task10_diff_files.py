import os
import tempfile


def diff_line_numbers(path_a: str, path_b: str) -> list[int]:
    with open(path_a, encoding="utf-8") as handle:
        lines_a = handle.read().splitlines()
    with open(path_b, encoding="utf-8") as handle:
        lines_b = handle.read().splitlines()
    diffs: list[int] = []
    for index in range(max(len(lines_a), len(lines_b))):
        left = lines_a[index] if index < len(lines_a) else None
        right = lines_b[index] if index < len(lines_b) else None
        if left != right:
            diffs.append(index + 1)
    return diffs


def main() -> None:
    path_a = tempfile.mktemp(suffix=".txt")
    path_b = tempfile.mktemp(suffix=".txt")
    with open(path_a, "w", encoding="utf-8") as handle:
        handle.write("строка 1\nстрока 2\nстрока 3\n")
    with open(path_b, "w", encoding="utf-8") as handle:
        handle.write("строка 1\nИЗМЕНЕНО\nстрока 3\nстрока 4\n")
    print("Отличающиеся строки:", diff_line_numbers(path_a, path_b))
    os.remove(path_a)
    os.remove(path_b)


if __name__ == "__main__":
    main()
