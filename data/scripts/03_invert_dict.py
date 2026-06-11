from collections import defaultdict
from typing import Any


def invert_dict(data: dict[Any, Any]) -> dict[Any, list[Any]]:
    inverted: defaultdict[Any, list[Any]] = defaultdict(list)
    for key, value in data.items():
        inverted[value].append(key)
    return dict(inverted)


def main() -> None:
    data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
    print(invert_dict(data))
    print(invert_dict({}))


if __name__ == "__main__":
    main()
