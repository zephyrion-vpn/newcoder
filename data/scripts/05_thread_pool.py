import queue
import threading
from typing import Any, Callable


class ThreadPool:
    def __init__(self, num_workers: int) -> None:
        self._tasks: queue.Queue = queue.Queue()
        self._results: queue.Queue = queue.Queue()
        self._workers: list[threading.Thread] = []
        self._shutdown = False
        for _ in range(num_workers):
            worker = threading.Thread(target=self._worker_loop, daemon=True)
            worker.start()
            self._workers.append(worker)

    def submit(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> None:
        self._tasks.put((func, args, kwargs))

    def _worker_loop(self) -> None:
        while True:
            item = self._tasks.get()
            if item is None:
                self._tasks.task_done()
                return
            func, args, kwargs = item
            try:
                self._results.put(("ok", func(*args, **kwargs)))
            except Exception as error:  # noqa: BLE001
                self._results.put(("error", error))
            finally:
                self._tasks.task_done()

    def results(self) -> list[Any]:
        self._tasks.join()
        collected = []
        while not self._results.empty():
            collected.append(self._results.get())
        return collected

    def shutdown(self) -> None:
        for _ in self._workers:
            self._tasks.put(None)
        for worker in self._workers:
            worker.join()


def main() -> None:
    pool = ThreadPool(num_workers=4)
    for i in range(10):
        pool.submit(lambda x: x * x, i)
    results = pool.results()
    values = sorted(value for status, value in results if status == "ok")
    print(f"Задач: 10, результатов: {len(results)}")
    print(f"Квадраты: {values}")
    pool.shutdown()


if __name__ == "__main__":
    main()
