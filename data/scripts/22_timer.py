import time
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def measure(label: str = "блок") -> Iterator[None]:
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"[{label}] время: {elapsed * 1_000_000:.1f} мкс ({elapsed:.6f} с)")


def main() -> None:
    with measure("сумма миллиона"):
        total = sum(range(1_000_000))
    print("Результат:", total)

    with measure("сортировка"):
        data = sorted(range(100_000, 0, -1))
    print("Отсортировано элементов:", len(data))


if __name__ == "__main__":
    main()
