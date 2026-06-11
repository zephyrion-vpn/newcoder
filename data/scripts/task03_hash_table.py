from typing import Any, Hashable, Iterator

_EMPTY = object()
_DELETED = object()
_MAX_LOAD_FACTOR = 0.7


class HashTable:
    def __init__(self, capacity: int = 8) -> None:
        self._capacity = max(8, capacity)
        self._size = 0
        self._keys: list[Any] = [_EMPTY] * self._capacity
        self._values: list[Any] = [None] * self._capacity

    def _slot_for(self, key: Hashable) -> tuple[int, bool]:
        index = hash(key) % self._capacity
        first_free = -1
        for _ in range(self._capacity):
            current = self._keys[index]
            if current is _EMPTY:
                return (index if first_free == -1 else first_free), False
            if current is _DELETED:
                if first_free == -1:
                    first_free = index
            elif current == key:
                return index, True
            index = (index + 1) % self._capacity
        return first_free, False

    def _resize(self, new_capacity: int) -> None:
        old_keys, old_values = self._keys, self._values
        self._capacity = new_capacity
        self._keys = [_EMPTY] * new_capacity
        self._values = [None] * new_capacity
        self._size = 0
        for key, value in zip(old_keys, old_values):
            if key is not _EMPTY and key is not _DELETED:
                self.put(key, value)

    def put(self, key: Hashable, value: Any) -> None:
        if (self._size + 1) / self._capacity > _MAX_LOAD_FACTOR:
            self._resize(self._capacity * 2)
        index, found = self._slot_for(key)
        if not found:
            self._size += 1
        self._keys[index] = key
        self._values[index] = value

    def get(self, key: Hashable, default: Any = None) -> Any:
        index, found = self._slot_for(key)
        return self._values[index] if found else default

    def delete(self, key: Hashable) -> None:
        index, found = self._slot_for(key)
        if not found:
            raise KeyError(key)
        self._keys[index] = _DELETED
        self._values[index] = None
        self._size -= 1

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.put(key, value)

    def __getitem__(self, key: Hashable) -> Any:
        index, found = self._slot_for(key)
        if not found:
            raise KeyError(key)
        return self._values[index]

    def __contains__(self, key: Hashable) -> bool:
        return self._slot_for(key)[1]

    def __len__(self) -> int:
        return self._size

    def items(self) -> Iterator[tuple[Hashable, Any]]:
        for key, value in zip(self._keys, self._values):
            if key is not _EMPTY and key is not _DELETED:
                yield key, value


def main() -> None:
    table = HashTable()
    for i in range(10):
        table[f"key{i}"] = i * i
    print("len:", len(table), "capacity:", table._capacity)
    print("key3:", table["key3"])
    table.delete("key3")
    print("contains key3:", "key3" in table)
    print("get key3:", table.get("key3", "нет"))


if __name__ == "__main__":
    main()
