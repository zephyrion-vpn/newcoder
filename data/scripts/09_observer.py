from __future__ import annotations

from typing import Any


class Observer:
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, state: Any) -> None:
        print(f"{self.name} получил уведомление: {state}")


class Subject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._state: Any = None

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def set_state(self, state: Any) -> None:
        self._state = state
        self._notify()

    def _notify(self) -> None:
        for observer in self._observers:
            observer.update(self._state)


def main() -> None:
    subject = Subject()
    a = Observer("Наблюдатель A")
    b = Observer("Наблюдатель B")
    subject.attach(a)
    subject.attach(b)
    subject.set_state("состояние 1")
    subject.detach(a)
    subject.set_state("состояние 2")


if __name__ == "__main__":
    main()
