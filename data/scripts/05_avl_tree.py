from typing import Optional


class AVLNode:
    __slots__ = ("key", "left", "right", "height")

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.height = 1


class AVLTree:
    def __init__(self) -> None:
        self.root: Optional[AVLNode] = None

    def insert(self, key: int) -> None:
        self.root = self._insert(self.root, key)

    def _height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _balance(self, node: AVLNode) -> int:
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node: AVLNode) -> None:
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        assert x is not None
        y.left = x.right
        x.right = y
        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        assert y is not None
        x.right = y.left
        y.left = x
        self._update_height(x)
        self._update_height(y)
        return y

    def _insert(self, node: Optional[AVLNode], key: int) -> AVLNode:
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        self._update_height(node)
        balance = self._balance(node)
        if balance > 1 and node.left and key < node.left.key:
            return self._rotate_right(node)
        if balance < -1 and node.right and key > node.right.key:
            return self._rotate_left(node)
        if balance > 1 and node.left and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and node.right and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def inorder(self) -> list[int]:
        result: list[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[AVLNode], result: list[int]) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def is_balanced(self) -> bool:
        return self._check(self.root)

    def _check(self, node: Optional[AVLNode]) -> bool:
        if node is None:
            return True
        if abs(self._balance(node)) > 1:
            return False
        return self._check(node.left) and self._check(node.right)


def main() -> None:
    tree = AVLTree()
    for key in [10, 20, 30, 40, 50, 25]:
        tree.insert(key)
    print("In-order:", tree.inorder())
    print("Корень:", tree.root.key if tree.root else None)
    print("Сбалансировано:", tree.is_balanced())
    print("Высота:", tree._height(tree.root))


if __name__ == "__main__":
    main()
