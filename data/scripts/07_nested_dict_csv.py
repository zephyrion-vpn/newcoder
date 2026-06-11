import csv
import os
import tempfile
from collections import defaultdict
from typing import Any


def build_nested(path: str) -> dict[str, dict[str, list[str]]]:
    result: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            result[row["country"]][row["city"]].append(row["name"])
    return {country: dict(cities) for country, cities in result.items()}


def main() -> None:
    path = os.path.join(tempfile.mkdtemp(), "people.csv")
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["name", "country", "city"])
        writer.writerows([
            ["Анна", "Россия", "Москва"],
            ["Борис", "Россия", "Москва"],
            ["Виктор", "Россия", "Казань"],
            ["Джон", "США", "Нью-Йорк"],
        ])
    nested = build_nested(path)
    for country, cities in nested.items():
        print(f"{country}: {dict(cities)}")


if __name__ == "__main__":
    main()
