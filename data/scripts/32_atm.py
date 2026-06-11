import sys
from typing import Optional


class ATM:
    def __init__(self, pin: str, balance: int = 0) -> None:
        self._pin = pin
        self._balance = balance
        self._authenticated = False
        self.history: list[str] = []

    def authenticate(self, pin: str, attempts_left: int = 3) -> bool:
        self._authenticated = pin == self._pin
        if self._authenticated:
            self.history.append("успешная авторизация")
        return self._authenticated

    def _require_auth(self) -> None:
        if not self._authenticated:
            raise PermissionError("требуется авторизация")

    def check_balance(self) -> int:
        self._require_auth()
        self.history.append(f"проверка баланса: {self._balance}")
        return self._balance

    def withdraw(self, amount: int) -> int:
        self._require_auth()
        if amount <= 0:
            raise ValueError("сумма должна быть положительной")
        if amount % 100 != 0:
            raise ValueError("сумма должна быть кратна 100")
        if amount > self._balance:
            raise ValueError("недостаточно средств")
        self._balance -= amount
        self.history.append(f"снятие: {amount}, остаток: {self._balance}")
        return self._balance


def _demo() -> None:
    atm = ATM(pin="1234", balance=5000)
    print("Демо-режим банкомата:")
    print("Неверный PIN 0000:", atm.authenticate("0000"))
    print("Верный PIN 1234:", atm.authenticate("1234"))
    print("Баланс:", atm.check_balance())
    print("Снятие 1500:", atm.withdraw(1500))
    for bad, reason in [(150, "не кратно 100"), (999999, "превышает баланс")]:
        try:
            atm.withdraw(bad)
        except ValueError as error:
            print(f"Снятие {bad} отклонено ({reason}): {error}")
    print("История операций:")
    for entry in atm.history:
        print(f"   - {entry}")


def _interactive() -> None:
    atm = ATM(pin="1234", balance=5000)
    for _ in range(3):
        try:
            pin = input("Введите PIN: ")
        except EOFError:
            return
        if atm.authenticate(pin):
            break
        print("Неверный PIN.")
    else:
        print("Карта заблокирована.")
        return
    while True:
        try:
            choice = input("[1] баланс [2] снять [3] история [0] выход: ").strip()
        except EOFError:
            return
        if choice == "0":
            return
        if choice == "1":
            print("Баланс:", atm.check_balance())
        elif choice == "2":
            try:
                print("Остаток:", atm.withdraw(int(input("Сумма: "))))
            except ValueError as error:
                print("Ошибка:", error)
        elif choice == "3":
            for entry in atm.history:
                print("   -", entry)


def main() -> None:
    if sys.stdin.isatty():
        _interactive()
    else:
        _demo()


if __name__ == "__main__":
    main()
