from typing import Iterator


class Countdown:
    def __init__(self, start: int) -> None:
        if start < 0:
            raise ValueError("start должен быть неотрицательным.")
        self.start = start

    def __iter__(self) -> Iterator[int]:
        current = self.start
        while current >= 0:
            yield current
            current -= 1


def main() -> None:
    print(list(Countdown(5)))
    print([n for n in Countdown(3)])


if __name__ == "__main__":
    main()
