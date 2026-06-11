import csv
import json
import os
import tempfile


def csv_to_json(csv_path: str, json_path: str) -> int:
    with open(csv_path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    with open(json_path, "w", encoding="utf-8") as handle:
        json.dump(rows, handle, ensure_ascii=False, indent=4)
    return len(rows)


def main() -> None:
    folder = tempfile.mkdtemp()
    csv_path = os.path.join(folder, "data.csv")
    json_path = os.path.join(folder, "data.json")
    with open(csv_path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["name", "city"])
        writer.writerows([["Анна", "Москва"], ["Борис", "Казань"]])
    count = csv_to_json(csv_path, json_path)
    print(f"Преобразовано записей: {count}")
    with open(json_path, encoding="utf-8") as handle:
        print(handle.read())


if __name__ == "__main__":
    main()
