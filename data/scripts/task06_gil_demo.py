import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from typing import Callable


def cpu_bound(iterations: int) -> int:
    total = 0
    for i in range(iterations):
        total += i * i
    return total


def _benchmark(executor_factory: Callable[..., object], workers: int, payloads: list[int]) -> float:
    start = time.perf_counter()
    with executor_factory(max_workers=workers) as executor:
        list(executor.map(cpu_bound, payloads))
    return time.perf_counter() - start


def main() -> None:
    workers = 4
    payloads = [3_000_000] * 4

    sequential_start = time.perf_counter()
    for payload in payloads:
        cpu_bound(payload)
    sequential = time.perf_counter() - sequential_start

    threaded = _benchmark(ThreadPoolExecutor, workers, payloads)
    multiprocess = _benchmark(ProcessPoolExecutor, workers, payloads)

    print(f"Последовательно:  {sequential:.2f}s")
    print(f"threading:       {threaded:.2f}s  (GIL блокирует CPU-bound)")
    print(f"multiprocessing: {multiprocess:.2f}s")
    print(f"Ускорение multiprocessing относительно threading: {threaded / multiprocess:.2f}x")


if __name__ == "__main__":
    main()
