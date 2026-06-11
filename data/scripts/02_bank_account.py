class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")
        self.__balance = balance

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.__balance:
            raise InsufficientFundsError("Недостаточно средств.")
        self.__balance -= amount


def main() -> None:
    account = BankAccount(100)
    account.deposit(50)
    print(f"Баланс: {account.balance}")
    account.withdraw(30)
    print(f"Баланс: {account.balance}")
    try:
        account.withdraw(1000)
    except InsufficientFundsError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
