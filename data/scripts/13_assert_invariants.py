from numbers import Real
from typing import Sequence


def average(values: Sequence[float]) -> float:
    assert len(values) > 0, "список не должен быть пустым"
    assert all(isinstance(v, Real) and not isinstance(v, bool) for v in values), \
        "все элементы должны быть числами"
    result = sum(values) / len(values)
    assert isinstance(result, Real), "результат должен быть числом"
    return result


def main() -> None:
    print("Среднее [1, 2, 3, 4]:", average([1, 2, 3, 4]))

    for bad in ([], [1, "два", 3], [True, False]):
        try:
            average(bad)
        except AssertionError as error:
            print(f"AssertionError для {bad!r}: {error}")


if __name__ == "__main__":
    main()
