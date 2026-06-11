from typing import Any


def remove_duplicates(items: list[Any]) -> list[Any]:
    return list(dict.fromkeys(items))


def main() -> None:
    print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))
    print(remove_duplicates(["a", "b", "a", "c", "b"]))
    print(remove_duplicates([]))


if __name__ == "__main__":
    main()
