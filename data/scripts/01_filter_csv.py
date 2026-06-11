import csv
import os
import tempfile


def filter_csv(source: str, destination: str, min_price: float) -> int:
    with open(source, newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or []
        rows = [row for row in reader if float(row["price"]) > min_price]
    with open(destination, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def main() -> None:
    folder = tempfile.mkdtemp()
    source = os.path.join(folder, "products.csv")
    destination = os.path.join(folder, "expensive.csv")
    with open(source, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["name", "price"])
        writer.writerows([["Яблоко", "50"], ["Ноутбук", "1500"], ["Книга", "120"], ["Ручка", "30"]])
    count = filter_csv(source, destination, 100)
    print(f"Отобрано строк: {count}")
    with open(destination, encoding="utf-8") as handle:
        print(handle.read().strip())


if __name__ == "__main__":
    main()
