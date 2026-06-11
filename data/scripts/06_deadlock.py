import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def _ordered_locks(*locks: threading.Lock) -> list[threading.Lock]:
    # Глобальный порядок захвата по id предотвращает deadlock.
    return sorted(locks, key=id)


def safe_worker(name: str, first: threading.Lock, second: threading.Lock, counter: list[int]) -> None:
    for _ in range(1000):
        a, b = _ordered_locks(first, second)
        with a:
            with b:
                counter[0] += 1


def main() -> None:
    counter = [0]
    t1 = threading.Thread(target=safe_worker, args=("T1", lock_a, lock_b, counter))
    t2 = threading.Thread(target=safe_worker, args=("T2", lock_b, lock_a, counter))
    start = time.perf_counter()
    t1.start()
    t2.start()
    t1.join(timeout=5)
    t2.join(timeout=5)
    elapsed = time.perf_counter() - start
    deadlocked = t1.is_alive() or t2.is_alive()
    print(f"Deadlock произошёл: {deadlocked}")
    print(f"Счётчик: {counter[0]} (ожидалось 2000)")
    print(f"Время: {elapsed:.3f} с")


if __name__ == "__main__":
    main()
