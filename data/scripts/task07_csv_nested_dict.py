import csv
import os
import tempfile
from collections import defaultdict


def build_nested(path: str, outer: str, inner: str, value: str) -> dict[str, dict[str, list[str]]]:
    nested: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            nested[row[outer]][row[inner]].append(row[value])
    return {key: dict(value_map) for key, value_map in nested.items()}


def main() -> None:
    path = tempfile.mktemp(suffix=".csv")
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["country", "city", "name"])
        writer.writerows(
            [
                ["Россия", "Москва", "Анна"],
                ["Россия", "Москва", "Иван"],
                ["Россия", "Казань", "Ольга"],
                ["США", "Нью-Йорк", "John"],
            ]
        )
    nested = build_nested(path, outer="country", inner="city", value="name")
    for country, cities in nested.items():
        print(country, "->", dict(cities))
    os.remove(path)


if __name__ == "__main__":
    main()
