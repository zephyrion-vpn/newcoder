from __future__ import annotations

from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def insert_coin(self, machine: VendingMachine) -> None:
        ...

    @abstractmethod
    def select(self, machine: VendingMachine, exact_change: bool) -> None:
        ...


class WaitingCoinState(State):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("Монета принята")
        machine.state = SelectionState()

    def select(self, machine: VendingMachine, exact_change: bool) -> None:
        print("Сначала внесите монету")


class SelectionState(State):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("Монета уже внесена")

    def select(self, machine: VendingMachine, exact_change: bool) -> None:
        if exact_change:
            machine.state = DispensingState()
        else:
            machine.state = NoChangeState()
        machine.state.select(machine, exact_change)


class DispensingState(State):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("Подождите выдачи товара")

    def select(self, machine: VendingMachine, exact_change: bool) -> None:
        print("Товар выдан")
        machine.state = WaitingCoinState()


class NoChangeState(State):
    def insert_coin(self, machine: VendingMachine) -> None:
        print("Нет сдачи, монета возвращена")

    def select(self, machine: VendingMachine, exact_change: bool) -> None:
        print("Нет сдачи — внесите точную сумму")
        machine.state = WaitingCoinState()


class VendingMachine:
    def __init__(self) -> None:
        self.state: State = WaitingCoinState()

    def insert_coin(self) -> None:
        self.state.insert_coin(self)

    def select(self, exact_change: bool = True) -> None:
        self.state.select(self, exact_change)


def main() -> None:
    machine = VendingMachine()
    print("— Успешная покупка —")
    machine.insert_coin()
    machine.select(exact_change=True)
    print("— Нет сдачи —")
    machine.insert_coin()
    machine.select(exact_change=False)


if __name__ == "__main__":
    main()
