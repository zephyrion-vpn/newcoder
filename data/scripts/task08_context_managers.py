import time
from contextlib import contextmanager
from typing import Iterator


class Timer:
    def __init__(self, label: str) -> None:
        self.label = label
        self.elapsed = 0.0
        self._start = 0.0

    def __enter__(self) -> "Timer":
        self._start = time.perf_counter()
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> bool:
        self.elapsed = time.perf_counter() - self._start
        print(f"[класс] {self.label}: {self.elapsed * 1000:.2f} мс")
        return False


@contextmanager
def timer(label: str) -> Iterator[None]:
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"[contextmanager] {label}: {(time.perf_counter() - start) * 1000:.2f} мс")


def main() -> None:
    with Timer("блок A"):
        sum(range(1_000_000))
    with timer("блок B"):
        sum(range(1_000_000))


if __name__ == "__main__":
    main()
