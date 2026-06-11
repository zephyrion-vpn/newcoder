import random
import threading
import time


def worker(barrier: threading.Barrier, worker_id: int, started: dict[int, float]) -> None:
    setup_time = random.uniform(0.1, 0.6)
    time.sleep(setup_time)
    print(f"Поток {worker_id} готов (подготовка {setup_time:.2f}s)")
    barrier.wait()
    started[worker_id] = time.perf_counter()


def main() -> None:
    count = 5
    barrier = threading.Barrier(count)
    started: dict[int, float] = {}
    threads = [
        threading.Thread(target=worker, args=(barrier, i, started)) for i in range(count)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    spread_ms = (max(started.values()) - min(started.values())) * 1000
    print(f"Все потоки стартовали в пределах {spread_ms:.2f} мс")


if __name__ == "__main__":
    main()
