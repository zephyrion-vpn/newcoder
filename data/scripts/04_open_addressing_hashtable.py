from typing import Any, Optional

_EMPTY = object()
_DELETED = object()


class DoubleHashTable:
    def __init__(self, capacity: int = 8) -> None:
        self._capacity = self._next_prime(capacity)
        self._keys: list[Any] = [_EMPTY] * self._capacity
        self._values: list[Any] = [None] * self._capacity
        self._size = 0

    @staticmethod
    def _is_prime(n: int) -> bool:
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def _next_prime(self, n: int) -> int:
        while not self._is_prime(n):
            n += 1
        return n

    def _hash1(self, key: Any) -> int:
        return hash(key) % self._capacity

    def _hash2(self, key: Any) -> int:
        prime = self._capacity - 1
        return prime - (hash(key) % prime)

    def _probe(self, key: Any):
        h1 = self._hash1(key)
        h2 = self._hash2(key)
        for i in range(self._capacity):
            yield (h1 + i * h2) % self._capacity

    def put(self, key: Any, value: Any) -> None:
        if (self._size + 1) / self._capacity > 0.7:
            self._resize()
        first_deleted = None
        for index in self._probe(key):
            slot = self._keys[index]
            if slot is _EMPTY:
                target = first_deleted if first_deleted is not None else index
                self._keys[target] = key
                self._values[target] = value
                self._size += 1
                return
            if slot is _DELETED:
                if first_deleted is None:
                    first_deleted = index
                continue
            if slot == key:
                self._values[index] = value
                return
        raise RuntimeError("Таблица переполнена.")

    def get(self, key: Any, default: Any = None) -> Any:
        for index in self._probe(key):
            slot = self._keys[index]
            if slot is _EMPTY:
                return default
            if slot is _DELETED:
                continue
            if slot == key:
                return self._values[index]
        return default

    def delete(self, key: Any) -> bool:
        for index in self._probe(key):
            slot = self._keys[index]
            if slot is _EMPTY:
                return False
            if slot is _DELETED:
                continue
            if slot == key:
                self._keys[index] = _DELETED
                self._values[index] = None
                self._size -= 1
                return True
        return False

    def _resize(self) -> None:
        old_keys = self._keys
        old_values = self._values
        self._capacity = self._next_prime(self._capacity * 2)
        self._keys = [_EMPTY] * self._capacity
        self._values = [None] * self._capacity
        self._size = 0
        for key, value in zip(old_keys, old_values):
            if key is not _EMPTY and key is not _DELETED:
                self.put(key, value)

    def __len__(self) -> int:
        return self._size


def main() -> None:
    table = DoubleHashTable()
    for i in range(20):
        table.put(f"key-{i}", i * 10)

    print(f"Размер: {len(table)}")
    print(f"get('key-5'): {table.get('key-5')}")
    print(f"get('key-19'): {table.get('key-19')}")
    print(f"delete('key-5'): {table.delete('key-5')}")
    print(f"get('key-5') после удаления: {table.get('key-5')}")
    print(f"get('нет'): {table.get('нет', 'default')}")
    all_ok = all(table.get(f"key-{i}") == i * 10 for i in range(20) if i != 5)
    print(f"Все остальные ключи на месте: {all_ok}")


if __name__ == "__main__":
    main()
