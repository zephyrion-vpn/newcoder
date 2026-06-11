import json
import tempfile
from pathlib import Path
from typing import Any


def sort_json_file(path: Path, key: str, reverse: bool = False) -> list[dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("Ожидается JSON-массив объектов.")
    data.sort(key=lambda item: item[key], reverse=reverse)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
    return data


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    path = tmp / "people.json"
    sample = [
        {"name": "Carol", "age": 35},
        {"name": "Alice", "age": 28},
        {"name": "Bob", "age": 42},
    ]
    path.write_text(json.dumps(sample, ensure_ascii=False), encoding="utf-8")

    result = sort_json_file(path, key="age")
    print("Отсортировано по age:")
    for item in result:
        print(f"   {item['name']}: {item['age']}")
    print("\nФайл перезаписан. Содержимое:")
    print(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
