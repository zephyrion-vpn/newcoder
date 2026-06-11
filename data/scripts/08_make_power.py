from typing import Callable


def make_power(n: float) -> Callable[[float], float]:
    def power(base: float) -> float:
        return base ** n
    return power


def main() -> None:
    square = make_power(2)
    cube = make_power(3)
    print(square(5))
    print(cube(2))
    print(make_power(0.5)(16))


if __name__ == "__main__":
    main()
