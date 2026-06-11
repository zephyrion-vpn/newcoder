import sys
from collections.abc import Mapping


def deep_getsizeof(obj: object, seen: set[int] | None = None) -> int:
    if seen is None:
        seen = set()
    if id(obj) in seen:
        return 0
    seen.add(id(obj))
    size = sys.getsizeof(obj)
    if isinstance(obj, (str, bytes, bytearray)):
        return size
    if isinstance(obj, Mapping):
        for key, value in obj.items():
            size += deep_getsizeof(key, seen) + deep_getsizeof(value, seen)
    elif isinstance(obj, (tuple, list, set, frozenset)):
        for item in obj:
            size += deep_getsizeof(item, seen)
    return size


def to_columnar(rows: list[dict[str, object]]) -> dict[str, tuple]:
    if not rows:
        return {}
    keys = rows[0].keys()
    return {key: tuple(row[key] for row in rows) for key in keys}


def main() -> None:
    rows = [{"id": i, "value": i * 2, "label": "row"} for i in range(10_000)]
    columnar = to_columnar(rows)

    rows_size = deep_getsizeof(rows)
    columnar_size = deep_getsizeof(columnar)
    print(f"Список словарей: {rows_size / 1024:.1f} КБ")
    print(f"Словарь кортежей: {columnar_size / 1024:.1f} КБ")
    print(f"Экономия: {(1 - columnar_size / rows_size) * 100:.1f}%")

    try:
        import pandas as pd
    except ImportError:
        print("[fallback] pandas не найден — вариант с DataFrame пропущен")
        return
    frame = pd.DataFrame(rows)
    frame_size = frame.memory_usage(deep=True).sum()
    print(f"pandas DataFrame: {frame_size / 1024:.1f} КБ")


if __name__ == "__main__":
    main()
