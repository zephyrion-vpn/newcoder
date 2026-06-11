import itertools
import threading
from collections import Counter


class RoundRobinBalancer:
    def __init__(self, backends: list[str]) -> None:
        if not backends:
            raise ValueError("Нужен хотя бы один бэкенд.")
        self._backends = list(backends)
        self._cycle = itertools.cycle(self._backends)
        self._lock = threading.Lock()

    def get_backend(self) -> str:
        with self._lock:
            return next(self._cycle)


def main() -> None:
    balancer = RoundRobinBalancer(["srv-A", "srv-B", "srv-C"])
    distribution: Counter[str] = Counter()
    assignments = []

    for _ in range(9):
        backend = balancer.get_backend()
        distribution[backend] += 1
        assignments.append(backend)

    print("Порядок распределения:", assignments)
    print("Распределение:", dict(distribution))
    print("Равномерно:", len(set(distribution.values())) == 1)


if __name__ == "__main__":
    main()
