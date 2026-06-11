import csv
import os
import tempfile


def filter_csv(source: str, destination: str, column: str, threshold: float) -> int:
    written = 0
    with open(source, newline="", encoding="utf-8") as inp, open(
        destination, "w", newline="", encoding="utf-8"
    ) as out:
        reader = csv.DictReader(inp)
        if reader.fieldnames is None:
            raise ValueError("Пустой CSV-файл")
        writer = csv.DictWriter(out, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            try:
                value = float(row[column])
            except (KeyError, ValueError):
                continue
            if value > threshold:
                writer.writerow(row)
                written += 1
    return written


def main() -> None:
    source = tempfile.mktemp(suffix=".csv")
    destination = tempfile.mktemp(suffix=".csv")
    with open(source, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["name", "price"])
        writer.writerows([["яблоко", "50"], ["ноутбук", "1500"], ["книга", "120"]])
    count = filter_csv(source, destination, column="price", threshold=100)
    print(f"Отобрано строк: {count}")
    with open(destination, encoding="utf-8") as handle:
        print(handle.read().strip())
    os.remove(source)
    os.remove(destination)


if __name__ == "__main__":
    main()
