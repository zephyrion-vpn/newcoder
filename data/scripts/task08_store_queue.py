from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    name: str
    arrival_time: float
    service_duration: float


class Queue:
    def __init__(self) -> None:
        self._waiting: deque[Customer] = deque()
        self._clock = 0.0
        self._wait_times: list[float] = []

    def add_customer(self, name: str, arrival_time: float, service_duration: float) -> None:
        if service_duration <= 0:
            raise ValueError("Длительность обслуживания должна быть положительной.")
        if arrival_time < 0:
            raise ValueError("Время прихода не может быть отрицательным.")
        self._waiting.append(Customer(name, arrival_time, service_duration))

    def serve_customer(self) -> tuple[Customer, float] | None:
        if not self._waiting:
            return None
        customer = self._waiting.popleft()
        service_start = max(self._clock, customer.arrival_time)
        wait = service_start - customer.arrival_time
        self._clock = service_start + customer.service_duration
        self._wait_times.append(wait)
        return customer, wait

    @property
    def pending(self) -> int:
        return len(self._waiting)

    @property
    def average_wait_time(self) -> float:
        return sum(self._wait_times) / len(self._wait_times) if self._wait_times else 0.0


def main() -> None:
    queue = Queue()
    queue.add_customer("Анна", arrival_time=0, service_duration=4)
    queue.add_customer("Борис", arrival_time=1, service_duration=2)
    queue.add_customer("Вера", arrival_time=2, service_duration=5)

    while (served := queue.serve_customer()) is not None:
        customer, wait = served
        print(f"{customer.name}: ожидание {wait:g}")
    print(f"Среднее время ожидания: {queue.average_wait_time:.2f}")


if __name__ == "__main__":
    main()
