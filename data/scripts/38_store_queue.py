from collections import deque
from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    arrival: float
    service_time: float


class StoreQueue:
    def __init__(self) -> None:
        self._queue: deque[Customer] = deque()
        self._clock: float = 0.0
        self._wait_times: list[float] = []

    def add_customer(self, name: str, service_time: float) -> None:
        if service_time <= 0:
            raise ValueError("время обслуживания должно быть > 0")
        self._queue.append(Customer(name, arrival=self._clock, service_time=service_time))

    def serve_customer(self) -> str | None:
        if not self._queue:
            return None
        customer = self._queue.popleft()
        wait = self._clock - customer.arrival
        self._wait_times.append(wait)
        self._clock += customer.service_time
        return f"{customer.name} обслужен (ожидание {wait:.1f}, обслуживание {customer.service_time:.1f})"

    @property
    def average_wait(self) -> float:
        return sum(self._wait_times) / len(self._wait_times) if self._wait_times else 0.0

    def __len__(self) -> int:
        return len(self._queue)


def main() -> None:
    queue = StoreQueue()
    for name, service in [("Анна", 3), ("Борис", 5), ("Вера", 2), ("Глеб", 4)]:
        queue.add_customer(name, service)
    print(f"В очереди: {len(queue)} клиентов\n")

    while len(queue):
        print(queue.serve_customer())
    print(f"\nСреднее время ожидания: {queue.average_wait:.2f}")


if __name__ == "__main__":
    main()
