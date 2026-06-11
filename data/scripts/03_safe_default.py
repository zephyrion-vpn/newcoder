from typing import Any


def append_item(item: Any, target: list[Any] | None = None) -> list[Any]:
    if target is None:
        target = []
    target.append(item)
    return target


def main() -> None:
    print(append_item(1))
    print(append_item(2))
    shared = [10]
    print(append_item(20, shared))
    print(append_item(30, shared))


if __name__ == "__main__":
    main()
