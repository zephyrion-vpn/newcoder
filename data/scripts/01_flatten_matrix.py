from typing import Any


def flatten(matrix: list[list[Any]]) -> list[Any]:
    return [item for row in matrix for item in row]


def flatten_deep(data: Any) -> list[Any]:
    result: list[Any] = []
    stack = [iter(data)]
    while stack:
        try:
            item = next(stack[-1])
        except StopIteration:
            stack.pop()
            continue
        if isinstance(item, (list, tuple)):
            stack.append(iter(item))
        else:
            result.append(item)
    return result


def main() -> None:
    print(flatten([[1, 2], [3, 4]]))
    print(flatten([[1], [], [2, 3], [4, 5, 6]]))
    print(flatten_deep([1, [2, [3, [4, 5]]], 6]))


if __name__ == "__main__":
    main()
