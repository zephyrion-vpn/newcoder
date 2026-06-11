import json
import tempfile
from pathlib import Path


def sum_field(path: Path, field: str) -> tuple[float, int]:
    total = 0.0
    count = 0
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            value = obj.get(field)
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                continue
            total += value
            count += 1
    return total, count


def main() -> None:
    tmp = Path(tempfile.mkdtemp())
    path = tmp / "events.jsonl"
    records = [
        {"user": "a", "amount": 100},
        {"user": "b", "amount": 250.5},
        {"user": "c", "amount": 0},
        {"user": "d"},  # нет поля
        {"user": "e", "amount": 49.5},
    ]
    with open(path, "w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        handle.write("\n")  # пустая строка — должна игнорироваться

    total, count = sum_field(path, "amount")
    print(f"Обработано объектов с полем 'amount': {count}")
    print(f"Сумма 'amount': {total}")
    print(f"Ожидалось: {100 + 250.5 + 0 + 49.5}")


if __name__ == "__main__":
    main()
