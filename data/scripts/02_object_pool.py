from __future__ import annotations

import threading
from contextlib import contextmanager
from typing import Callable, Generic, Iterator, TypeVar

T = TypeVar("T")


class ObjectPool(Generic[T]):
    def __init__(self, factory: Callable[[], T], max_size: int = 5) -> None:
        self._factory = factory
        self._max_size = max_size
        self._available: list[T] = []
        self._in_use = 0
        self._created = 0
        self._lock = threading.Lock()

    def acquire(self) -> T:
        with self._lock:
            if self._available:
                obj = self._available.pop()
            else:
                obj = self._factory()
                self._created += 1
            self._in_use += 1
            return obj

    def release(self, obj: T) -> None:
        with self._lock:
            self._in_use -= 1
            if len(self._available) < self._max_size:
                self._available.append(obj)

    @contextmanager
    def borrow(self) -> Iterator[T]:
        obj = self.acquire()
        try:
            yield obj
        finally:
            self.release(obj)

    @property
    def created(self) -> int:
        return self._created


class ExpensiveConnection:
    _counter = 0

    def __init__(self) -> None:
        ExpensiveConnection._counter += 1
        self.id = ExpensiveConnection._counter


def main() -> None:
    pool: ObjectPool[ExpensiveConnection] = ObjectPool(ExpensiveConnection, max_size=3)

    for _ in range(10):
        with pool.borrow() as conn:
            _ = conn.id

    print(f"Выполнено операций: 10")
    print(f"Реально создано объектов: {pool.created} (благодаря переиспользованию)")


if __name__ == "__main__":
    main()
