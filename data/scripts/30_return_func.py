from typing import Callable


def multiplier(factor: int) -> Callable[[int], int]:
    def multiply(value: int) -> int:
        return value * factor

    return multiply


if __name__ == "__main__":
    double = multiplier(2)
    print(double(5))
