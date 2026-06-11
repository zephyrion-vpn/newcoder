from typing import Callable


def make_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def main() -> None:
    tick = make_counter()
    print(tick())
    print(tick())
    print(tick())
    other = make_counter()
    print(other())


if __name__ == "__main__":
    main()
