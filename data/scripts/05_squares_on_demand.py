from typing import Iterator


def squares_on_demand(n: int) -> Iterator[int]:
    for i in range(1, n + 1):
        yield i * i


def main() -> None:
    generator = squares_on_demand(5)
    for value in generator:
        print(value)
        command = input("Нажмите Enter для следующего (q для выхода): ")
        if command.strip().lower() == "q":
            break


if __name__ == "__main__":
    main()
