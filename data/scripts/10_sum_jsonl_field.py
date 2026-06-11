import json
import os
import tempfile
from numbers import Number


def sum_field(path: str, field: str) -> float:
    total: float = 0
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            value = record.get(field)
            if isinstance(value, Number) and not isinstance(value, bool):
                total += value
    return total


def main() -> None:
    path = os.path.join(tempfile.mkdtemp(), "orders.jsonl")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write('{"id": 1, "amount": 100}\n')
        handle.write('{"id": 2, "amount": 250.5}\n')
        handle.write('\n')
        handle.write('{"id": 3, "amount": 75}\n')
    print(f"Сумма поля amount: {sum_field(path, 'amount')}")


if __name__ == "__main__":
    main()
