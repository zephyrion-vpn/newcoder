import time
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def measure(label: str = "Блок") -> Iterator[None]:
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label}: {elapsed * 1_000_000:.1f} мкс ({elapsed:.6f} с)")


def main() -> None:
    with measure("Сумма квадратов"):
        total = sum(i * i for i in range(100_000))
    print(f"Результат: {total}")


if __name__ == "__main__":
    main()
