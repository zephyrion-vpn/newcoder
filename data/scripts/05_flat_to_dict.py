from typing import Any


def flat_to_dict(items: list[Any]) -> dict[Any, Any]:
    if len(items) % 2 != 0:
        raise ValueError("Список должен содержать чётное число элементов.")
    iterator = iter(items)
    return dict(zip(iterator, iterator))


def main() -> None:
    print(flat_to_dict(["a", 1, "b", 2, "c", 3]))
    print(flat_to_dict([]))


if __name__ == "__main__":
    main()
