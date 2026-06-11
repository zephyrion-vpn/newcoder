from typing import Any


def chunk_list(lst: list[Any], n: int) -> list[list[Any]]:
    if n < 1:
        raise ValueError("Размер части должен быть положительным.")
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def main() -> None:
    print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))
    print(chunk_list([1, 2, 3, 4], 2))
    print(chunk_list([], 3))


if __name__ == "__main__":
    main()
