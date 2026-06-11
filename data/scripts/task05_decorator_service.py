from abc import ABC, abstractmethod
from typing import Any


class Service(ABC):
    @abstractmethod
    def operation(self, value: int) -> int:
        ...


class ComputationService(Service):
    def operation(self, value: int) -> int:
        total = 0
        for i in range(value):
            total += i
        return total


class ServiceDecorator(Service):
    def __init__(self, wrapped: Service) -> None:
        self._wrapped = wrapped

    def operation(self, value: int) -> int:
        return self._wrapped.operation(value)


class LoggingDecorator(ServiceDecorator):
    def operation(self, value: int) -> int:
        print(f"[log] вызов operation({value})")
        result = self._wrapped.operation(value)
        print(f"[log] результат = {result}")
        return result


class CachingDecorator(ServiceDecorator):
    def __init__(self, wrapped: Service) -> None:
        super().__init__(wrapped)
        self._cache: dict[int, Any] = {}

    def operation(self, value: int) -> int:
        if value in self._cache:
            print(f"[cache] попадание для {value}")
            return self._cache[value]
        result = self._wrapped.operation(value)
        self._cache[value] = result
        return result


def main() -> None:
    service: Service = LoggingDecorator(CachingDecorator(ComputationService()))
    print("итог:", service.operation(1000))
    print("итог:", service.operation(1000))


if __name__ == "__main__":
    main()
