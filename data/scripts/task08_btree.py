import pickle
import tempfile
from typing import Any


class BTreeNode:
    __slots__ = ("keys", "children", "leaf")

    def __init__(self, leaf: bool = True) -> None:
        self.keys: list[int] = []
        self.children: list[BTreeNode] = []
        self.leaf = leaf


class BTree:
    def __init__(self, t: int = 2) -> None:
        if t < 2:
            raise ValueError("Минимальная степень t = 2")
        self.t = t
        self.root = BTreeNode(leaf=True)

    def search(self, key: int, node: BTreeNode | None = None) -> bool:
        node = node if node is not None else self.root
        index = 0
        while index < len(node.keys) and key > node.keys[index]:
            index += 1
        if index < len(node.keys) and node.keys[index] == key:
            return True
        if node.leaf:
            return False
        return self.search(key, node.children[index])

    def insert(self, key: int) -> None:
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)

    def _split_child(self, parent: BTreeNode, index: int) -> None:
        t = self.t
        child = parent.children[index]
        sibling = BTreeNode(leaf=child.leaf)
        parent.keys.insert(index, child.keys[t - 1])
        parent.children.insert(index + 1, sibling)
        sibling.keys = child.keys[t:]
        child.keys = child.keys[: t - 1]
        if not child.leaf:
            sibling.children = child.children[t:]
            child.children = child.children[:t]

    def _insert_non_full(self, node: BTreeNode, key: int) -> None:
        index = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while index >= 0 and key < node.keys[index]:
                node.keys[index + 1] = node.keys[index]
                index -= 1
            node.keys[index + 1] = key
        else:
            while index >= 0 and key < node.keys[index]:
                index -= 1
            index += 1
            if len(node.children[index].keys) == 2 * self.t - 1:
                self._split_child(node, index)
                if key > node.keys[index]:
                    index += 1
            self._insert_non_full(node.children[index], key)

    def save(self, path: str) -> None:
        with open(path, "wb") as handle:
            pickle.dump(self, handle)

    @staticmethod
    def load(path: str) -> "BTree":
        with open(path, "rb") as handle:
            return pickle.load(handle)


def main() -> None:
    tree = BTree(t=2)
    for key in [10, 20, 5, 6, 12, 30, 7, 17, 3, 25]:
        tree.insert(key)
    path = tempfile.mktemp(suffix=".btree")
    tree.save(path)
    restored = BTree.load(path)
    print("Ищем 6:", restored.search(6))
    print("Ищем 99:", restored.search(99))
    print("Корневые ключи:", restored.root.keys)


if __name__ == "__main__":
    main()
