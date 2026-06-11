import sys
from collections.abc import Mapping


def deep_getsizeof(obj: object, seen: set[int] | None = None) -> int:
    if seen is None:
        seen = set()
    identifier = id(obj)
    if identifier in seen:
        return 0
    seen.add(identifier)
    size = sys.getsizeof(obj)
    if isinstance(obj, (str, bytes, bytearray)):
        return size
    if isinstance(obj, Mapping):
        for key, value in obj.items():
            size += deep_getsizeof(key, seen) + deep_getsizeof(value, seen)
    elif isinstance(obj, (tuple, list, set, frozenset)):
        for item in obj:
            size += deep_getsizeof(item, seen)
    if hasattr(obj, "__dict__"):
        size += deep_getsizeof(vars(obj), seen)
    if hasattr(obj, "__slots__"):
        for slot in obj.__slots__:
            if hasattr(obj, slot):
                size += deep_getsizeof(getattr(obj, slot), seen)
    return size


def main() -> None:
    nested = {
        "numbers": list(range(100)),
        "text": "привет" * 10,
        "nested": {"a": (1, 2, 3), "b": [{"x": i} for i in range(10)]},
    }
    shared = [1, 2, 3]
    with_refs = [shared, shared, shared]
    print("Глубокий размер nested:", deep_getsizeof(nested), "байт")
    print("Поверхностный sys.getsizeof:", sys.getsizeof(nested), "байт")
    print("С повторными ссылками (считается один раз):", deep_getsizeof(with_refs), "байт")


if __name__ == "__main__":
    main()
