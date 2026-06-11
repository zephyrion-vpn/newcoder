from __future__ import annotations

from typing import Any, Iterator, Optional


class Node:
    def __init__(self, value: Any, left: Optional["Node"] = None, right: Optional["Node"] = None) -> None:
        self.value = value
        self.left = left
        self.right = right


def in_order(node: Optional[Node]) -> Iterator[Any]:
    if node is None:
        return
    yield from in_order(node.left)
    yield node.value
    yield from in_order(node.right)


def main() -> None:
    tree = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    print(list(in_order(tree)))


if __name__ == "__main__":
    main()
