from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, ticker: str, price: float) -> None:
        ...


class Stock:
    def __init__(self, ticker: str, price: float) -> None:
        self._ticker = ticker
        self._price = price
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value != self._price:
            self._price = value
            self._notify()

    def _notify(self) -> None:
        for observer in self._observers:
            observer.update(self._ticker, self._price)


class Investor(Observer):
    def __init__(self, name: str) -> None:
        self._name = name

    def update(self, ticker: str, price: float) -> None:
        print(f"{self._name}: {ticker} теперь {price:.2f}")


def main() -> None:
    stock = Stock("AAPL", 190.0)
    alice = Investor("Алиса")
    bob = Investor("Боб")
    stock.subscribe(alice)
    stock.subscribe(bob)
    stock.price = 192.5
    stock.unsubscribe(bob)
    stock.price = 188.0


if __name__ == "__main__":
    main()
