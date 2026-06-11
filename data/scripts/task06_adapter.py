from abc import ABC, abstractmethod
from typing import Any


class LegacySensor:
    def get_data(self) -> str:
        return "23.5;48;1012"


class DataSource(ABC):
    @abstractmethod
    def fetch(self) -> dict[str, float]:
        ...


class LegacySensorAdapter(DataSource):
    def __init__(self, sensor: LegacySensor) -> None:
        self._sensor = sensor

    def fetch(self) -> dict[str, float]:
        temperature, humidity, pressure = self._sensor.get_data().split(";")
        return {
            "temperature": float(temperature),
            "humidity": float(humidity),
            "pressure": float(pressure),
        }


def read_source(source: DataSource) -> dict[str, Any]:
    return source.fetch()


def main() -> None:
    adapter = LegacySensorAdapter(LegacySensor())
    print("Через новый интерфейс fetch():", read_source(adapter))


if __name__ == "__main__":
    main()
