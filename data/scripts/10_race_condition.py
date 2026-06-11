import threading
import time

ITERATIONS = 50_000
NUM_THREADS = 4
EXPECTED = ITERATIONS * NUM_THREADS


class UnsafeCounter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        current = self.value
        # Явная уступка GIL между чтением и записью надёжно провоцирует race.
        time.sleep(0)
        self.value = current + 1  # неатомарно: read-modify-write


class SafeCounter:
    def __init__(self) -> None:
        self.value = 0
        self._lock = threading.Lock()

    def increment(self) -> None:
        with self._lock:
            current = self.value
            time.sleep(0)
            self.value = current + 1


def run(counter) -> int:
    def task() -> None:
        for _ in range(ITERATIONS):
            counter.increment()

    threads = [threading.Thread(target=task) for _ in range(NUM_THREADS)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return counter.value


def main() -> None:
    unsafe = run(UnsafeCounter())
    safe = run(SafeCounter())
    print(f"Ожидаемое значение: {EXPECTED}")
    print(f"Без блокировки (race): {unsafe} — потеряно {EXPECTED - unsafe}")
    print(f"С блокировкой (Lock): {safe} — корректно: {safe == EXPECTED}")


if __name__ == "__main__":
    main()
