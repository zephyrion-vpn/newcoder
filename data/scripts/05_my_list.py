from typing import Any


class MyList(list):
    def second_max(self) -> Any:
        unique = sorted(set(self), reverse=True)
        if len(unique) < 2:
            raise ValueError("Нужно не менее двух различных элементов.")
        return unique[1]


def main() -> None:
    numbers = MyList([3, 1, 4, 1, 5, 9, 2, 6])
    print(numbers.second_max())
    print(MyList([10, 10, 7]).second_max())


if __name__ == "__main__":
    main()
