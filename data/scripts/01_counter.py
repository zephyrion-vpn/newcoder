from typing import Iterator


class Counter:
    def __init__(self, maximum: int) -> None:
        if maximum < 0:
            raise ValueError("maximum должен быть неотрицательным.")
        self.maximum = maximum

    def __iter__(self) -> Iterator[int]:
        self.current = 0
        return self

    def __next__(self) -> int:
        if self.current > self.maximum:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


def main() -> None:
    print(list(Counter(5)))
    print([n for n in Counter(0)])


if __name__ == "__main__":
    main()
