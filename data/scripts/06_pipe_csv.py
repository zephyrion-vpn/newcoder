import csv
import os
import tempfile


def read_pipe_delimited(path: str) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="|", quotechar='"')
        return list(reader)


def main() -> None:
    path = os.path.join(tempfile.mkdtemp(), "data.psv")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write('name|note\n')
        handle.write('Анна|обычная запись\n')
        handle.write('Борис|"внутри | есть черта"\n')
    for row in read_pipe_delimited(path):
        print(row)


if __name__ == "__main__":
    main()
