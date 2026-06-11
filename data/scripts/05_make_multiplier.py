from typing import Callable


def make_multiplier(n: float) -> Callable[[float], float]:
    def multiplier(value: float) -> float:
        return value * n
    return multiplier


def main() -> None:
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(double(5))
    print(triple(5))
    print(make_multiplier(0.5)(10))


if __name__ == "__main__":
    main()
