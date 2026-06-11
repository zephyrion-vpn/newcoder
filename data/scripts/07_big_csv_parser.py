import csv
import os
import tempfile
from typing import Iterator


def stream_rows(path: str) -> Iterator[list[str]]:
    with open(path, "r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        next(reader, None)  # пропускаем заголовок
        for row in reader:
            yield row


def aggregate(path: str, value_column: int) -> dict[str, float]:
    total = 0.0
    count = 0
    minimum = float("inf")
    maximum = float("-inf")
    for row in stream_rows(path):  # построчно: одна строка в памяти
        try:
            value = float(row[value_column])
        except (ValueError, IndexError):
            continue
        total += value
        count += 1
        minimum = min(minimum, value)
        maximum = max(maximum, value)
    return {
        "sum": total,
        "count": count,
        "avg": total / count if count else 0.0,
        "min": minimum if count else 0.0,
        "max": maximum if count else 0.0,
    }


def main() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["id", "name", "amount"])
        expected = 0.0
        for i in range(100_000):
            writer.writerow([i, f"item-{i}", i])
            expected += i
        path = handle.name

    stats = aggregate(path, value_column=2)
    print(f"Обработано строк: {stats['count']:,}")
    print(f"Сумма: {stats['sum']:,.0f} (ожидалось {expected:,.0f})")
    print(f"Среднее: {stats['avg']:.2f}, min={stats['min']:.0f}, max={stats['max']:.0f}")
    print(f"Совпадает: {stats['sum'] == expected}")
    print(f"Размер файла: {os.path.getsize(path) / 1024 / 1024:.1f} МБ, но в памяти всегда одна строка")
    print("Тот же подход работает для 10 ГБ: память не растёт с размером файла.")
    os.unlink(path)


if __name__ == "__main__":
    main()
