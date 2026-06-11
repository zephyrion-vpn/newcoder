import tempfile
from typing import Iterator


def extract(path: str) -> Iterator[str]:
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            yield line.rstrip("\n")


def transform(lines: Iterator[str]) -> Iterator[dict[str, object]]:
    for line in lines:
        name, _, amount = line.partition(",")
        if not amount:
            continue
        yield {"name": name.strip(), "amount": float(amount)}


def filter_large(records: Iterator[dict[str, object]], threshold: float) -> Iterator[dict[str, object]]:
    for record in records:
        if record["amount"] >= threshold:
            yield record


def run_pipeline(path: str, threshold: float) -> Iterator[dict[str, object]]:
    return filter_large(transform(extract(path)), threshold)


def main() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as handle:
        for i in range(1000):
            handle.write(f"item-{i},{i * 1.5}\n")
        path = handle.name

    pipeline = run_pipeline(path, threshold=1000.0)
    total = 0.0
    count = 0
    for record in pipeline:  # лениво, по одной записи
        total += float(record["amount"])
        count += 1

    print(f"Отфильтровано записей (amount >= 1000): {count}")
    print(f"Сумма: {total:.1f}")
    print("Пайплайн ленивый: данные никогда не загружаются целиком в память.")


if __name__ == "__main__":
    main()
