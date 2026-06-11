from typing import Callable


class CallCounter:
    def __init__(self) -> None:
        self.calls = 0

    def __call__(self, value: int) -> int:
        self.calls += 1
        return value * self.calls


def make_counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


def main() -> None:
    multiplier = CallCounter()
    print("Объект-счётчик:", multiplier(10), multiplier(10), multiplier(10))
    print("Всего вызовов:", multiplier.calls)

    counter = make_counter()
    print("Замыкание (nonlocal):", counter(), counter(), counter())


if __name__ == "__main__":
    main()
