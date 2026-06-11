from abc import ABC, abstractmethod


class DataReport(ABC):
    @abstractmethod
    def query(self, key: str) -> str:
        ...


class ExpensiveReport(DataReport):
    def __init__(self) -> None:
        print("Инициализация ресурсоёмкого объекта…")
        self._data = {"sales": "1200", "users": "350"}

    def query(self, key: str) -> str:
        return self._data.get(key, "нет данных")


class ReportProxy(DataReport):
    def __init__(self) -> None:
        self._report: ExpensiveReport | None = None
        self._cache: dict[str, str] = {}

    def query(self, key: str) -> str:
        if key in self._cache:
            print(f"[cache] {key}")
            return self._cache[key]
        if self._report is None:
            self._report = ExpensiveReport()
        value = self._report.query(key)
        self._cache[key] = value
        return value


def main() -> None:
    report = ReportProxy()
    print("Прокси создан, реальный объект ещё нет")
    print("sales =", report.query("sales"))
    print("sales =", report.query("sales"))
    print("users =", report.query("users"))


if __name__ == "__main__":
    main()
