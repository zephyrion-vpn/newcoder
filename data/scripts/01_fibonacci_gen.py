from itertools import islice
from typing import Iterator


def fibonacci() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main() -> None:
    print(list(islice(fibonacci(), 10)))


if __name__ == "__main__":
    main()
