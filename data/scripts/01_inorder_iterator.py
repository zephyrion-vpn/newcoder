from typing import Iterator, Optional


class TreeNode:
    __slots__ = ("value", "left", "right")

    def __init__(self, value: int, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None) -> None:
        self.value = value
        self.left = left
        self.right = right


class InOrderIterator:
    def __init__(self, root: Optional[TreeNode]) -> None:
        self._stack: list[TreeNode] = []
        self._push_left(root)

    def _push_left(self, node: Optional[TreeNode]) -> None:
        while node is not None:
            self._stack.append(node)
            node = node.left

    def __iter__(self) -> "InOrderIterator":
        return self

    def __next__(self) -> int:
        if not self._stack:
            raise StopIteration
        node = self._stack.pop()
        value = node.value
        if node.right is not None:
            self._push_left(node.right)
        return value


class BinaryTree:
    def __init__(self, root: Optional[TreeNode] = None) -> None:
        self.root = root

    def __iter__(self) -> InOrderIterator:
        return InOrderIterator(self.root)


def main() -> None:
    #        4
    #      /   \
    #     2     6
    #    / \   / \
    #   1   3 5   7
    root = TreeNode(
        4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(6, TreeNode(5), TreeNode(7)),
    )
    tree = BinaryTree(root)
    result = list(tree)
    print("In-order (без рекурсии):", result)
    print("Отсортировано:", result == sorted(result))


if __name__ == "__main__":
    main()
