import json
import os
import tempfile
from typing import Any


def sort_json_file(path: str, key: str, reverse: bool = False) -> list[dict[str, Any]]:
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("Ожидался список словарей.")
    data.sort(key=lambda item: item[key], reverse=reverse)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=4)
    return data


def main() -> None:
    path = os.path.join(tempfile.mkdtemp(), "people.json")
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(
            [{"name": "Анна", "age": 30}, {"name": "Борис", "age": 25}, {"name": "Виктор", "age": 40}],
            handle,
            ensure_ascii=False,
        )
    result = sort_json_file(path, "age")
    print([f"{item['name']}:{item['age']}" for item in result])


if __name__ == "__main__":
    main()
