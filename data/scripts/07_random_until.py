import random
from typing import Iterator


def random_until(target: int, low: int = 1, high: int = 6) -> Iterator[int]:
    if not low <= target <= high:
        raise ValueError("target должен быть в диапазоне [low, high].")
    while True:
        value = random.randint(low, high)
        yield value
        if value == target:
            return


def main() -> None:
    random.seed(42)
    values = list(random_until(3))
    print(values)
    print(f"Последнее выпавшее число: {values[-1]}")


if __name__ == "__main__":
    main()
