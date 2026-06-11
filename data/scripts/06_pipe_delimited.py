import csv
import io
import tempfile
from pathlib import Path
from typing import Any


def read_pipe_delimited(path: Path) -> list[dict[str, Any]]:
    with open(path, "r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="|", quotechar='"')
        return [dict(row) for row in reader]


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    path = tmp / "data.psv"
    content = io.StringIO()
    writer = csv.writer(content, delimiter="|", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["id", "name", "note"])
    writer.writerow(["1", "Alice", "обычная запись"])
    writer.writerow(["2", "Bob", "содержит | внутри кавычек"])
    writer.writerow(["3", "Carol", "ещё | одна | черта"])
    path.write_text(content.getvalue(), encoding="utf-8")

    print("Сырой файл:")
    print(path.read_text(encoding="utf-8"))

    rows = read_pipe_delimited(path)
    print("Разобрано:")
    for row in rows:
        print(f"   id={row['id']}, name={row['name']}, note={row['note']!r}")
    print(f"\nПоле 'note' у Bob сохранило черту: {'|' in rows[1]['note']}")


if __name__ == "__main__":
    main()
