import threading
import time
from contextlib import contextmanager
from typing import Iterator


class ReadWriteLock:
    def __init__(self) -> None:
        self._condition = threading.Condition()
        self._readers = 0
        self._writer_active = False
        self._waiting_writers = 0

    def acquire_read(self) -> None:
        with self._condition:
            while self._writer_active or self._waiting_writers > 0:
                self._condition.wait()
            self._readers += 1

    def release_read(self) -> None:
        with self._condition:
            self._readers -= 1
            if self._readers == 0:
                self._condition.notify_all()

    def acquire_write(self) -> None:
        with self._condition:
            self._waiting_writers += 1
            try:
                while self._writer_active or self._readers > 0:
                    self._condition.wait()
            finally:
                self._waiting_writers -= 1
            self._writer_active = True

    def release_write(self) -> None:
        with self._condition:
            self._writer_active = False
            self._condition.notify_all()

    @contextmanager
    def read_locked(self) -> Iterator[None]:
        self.acquire_read()
        try:
            yield
        finally:
            self.release_read()

    @contextmanager
    def write_locked(self) -> Iterator[None]:
        self.acquire_write()
        try:
            yield
        finally:
            self.release_write()


def main() -> None:
    lock = ReadWriteLock()
    shared = {"value": 0}

    def reader(reader_id: int) -> None:
        with lock.read_locked():
            print(f"Читатель {reader_id} видит {shared['value']}")
            time.sleep(0.1)

    def writer(writer_id: int) -> None:
        with lock.write_locked():
            shared["value"] += 1
            print(f"Писатель {writer_id} записал {shared['value']}")
            time.sleep(0.1)

    threads = [threading.Thread(target=reader, args=(i,)) for i in range(4)]
    threads += [threading.Thread(target=writer, args=(i,)) for i in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Итоговое значение:", shared["value"])


if __name__ == "__main__":
    main()
