import csv
import json
import tempfile
from pathlib import Path
from typing import Any


def csv_to_json(csv_path: Path, json_path: Path) -> list[dict[str, Any]]:
    with open(csv_path, "r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = [dict(row) for row in reader]
    with open(json_path, "w", encoding="utf-8") as handle:
        json.dump(rows, handle, ensure_ascii=False, indent=2)
    return rows


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    csv_path = tmp / "data.csv"
    json_path = tmp / "data.json"
    with open(csv_path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["name", "city", "age"])
        writer.writerow(["Alice", "Москва", "28"])
        writer.writerow(["Bob", "Питер", "42"])

    rows = csv_to_json(csv_path, json_path)
    print(f"Преобразовано строк: {len(rows)}")
    print("JSON-файл:")
    print(json_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
