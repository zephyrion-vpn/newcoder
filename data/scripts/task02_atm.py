from datetime import datetime


class ATMError(Exception):
    pass


class ATM:
    def __init__(self, pin: str, balance: int = 0) -> None:
        self._pin = pin
        self._balance = balance
        self._history: list[tuple[datetime, str]] = []

    def authenticate(self, pin: str) -> bool:
        return pin == self._pin

    @property
    def balance(self) -> int:
        return self._balance

    def withdraw(self, amount: int) -> int:
        if amount <= 0:
            raise ATMError("Сумма должна быть положительной.")
        if amount % 100 != 0:
            raise ATMError("Сумма должна быть кратна 100.")
        if amount > self._balance:
            raise ATMError("Недостаточно средств.")
        self._balance -= amount
        self._record(f"Снятие {amount}, остаток {self._balance}")
        return amount

    def _record(self, entry: str) -> None:
        self._history.append((datetime.now(), entry))

    @property
    def history(self) -> tuple[tuple[datetime, str], ...]:
        return tuple(self._history)


def _read_amount(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Введите целое число.")


def _authenticate(atm: ATM, attempts: int = 3) -> bool:
    for remaining in range(attempts - 1, -1, -1):
        if atm.authenticate(input("Введите ПИН-код: ").strip()):
            return True
        print(f"Неверный ПИН. Осталось попыток: {remaining}")
    return False


def main() -> None:
    atm = ATM(pin="1234", balance=5000)
    if not _authenticate(atm):
        print("Карта заблокирована.")
        return

    actions = {
        "1": "Проверить баланс",
        "2": "Снять наличные",
        "3": "История операций",
        "4": "Выход",
    }
    while True:
        print("\n" + "\n".join(f"{key}. {label}" for key, label in actions.items()))
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            print(f"Баланс: {atm.balance}")
        elif choice == "2":
            try:
                amount = atm.withdraw(_read_amount("Сумма снятия: "))
                print(f"Выдано {amount}. Остаток: {atm.balance}")
            except ATMError as error:
                print(f"Ошибка: {error}")
        elif choice == "3":
            if not atm.history:
                print("История пуста.")
            for moment, entry in atm.history:
                print(f"{moment:%Y-%m-%d %H:%M:%S} — {entry}")
        elif choice == "4":
            print("До свидания!")
            return
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()
