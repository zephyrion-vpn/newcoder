from typing import Callable


def make_counter() -> Callable[[], int]:
    count = 0

    def step() -> int:
        nonlocal count
        count += 1
        return count

    return step


if __name__ == "__main__":
    counter = make_counter()
    print(counter())
    print(counter())
