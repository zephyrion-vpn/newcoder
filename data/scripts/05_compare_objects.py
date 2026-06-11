import sys
import time
import tracemalloc
from collections import namedtuple
from dataclasses import dataclass
from typing import NamedTuple

N = 1_000_000

PointNT = namedtuple("PointNT", ["x", "y", "z"])


class PointTyped(NamedTuple):
    x: int
    y: int
    z: int


@dataclass
class PointDataclass:
    x: int
    y: int
    z: int


@dataclass
class PointSlots:
    __slots__ = ("x", "y", "z")
    x: int
    y: int
    z: int


class PointPlain:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z


def benchmark(name: str, factory) -> None:
    tracemalloc.start()
    start = time.perf_counter()
    objects = [factory(i, i, i) for i in range(N)]
    elapsed = time.perf_counter() - start
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    per_obj = sys.getsizeof(objects[0])
    print(f"{name:18} время={elapsed:5.2f}с  пик={peak / 1024 / 1024:6.1f} МБ  sizeof(1)={per_obj} байт")
    del objects


def main() -> None:
    print(f"Создание {N:,} объектов:\n")
    benchmark("namedtuple", PointNT)
    benchmark("NamedTuple", PointTyped)
    benchmark("dataclass", PointDataclass)
    benchmark("dataclass+slots", PointSlots)
    benchmark("plain class", PointPlain)
    print("\nВывод: __slots__ и namedtuple заметно экономят память по сравнению с обычным __dict__.")


if __name__ == "__main__":
    main()
