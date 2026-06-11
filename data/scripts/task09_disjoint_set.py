class DisjointSet:
    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("Размер не может быть отрицательным.")
        self._parent = list(range(size))
        self._rank = [0] * size
        self._sets = size

    def find(self, x: int) -> int:
        root = x
        while self._parent[root] != root:
            root = self._parent[root]
        while self._parent[x] != root:
            self._parent[x], x = root, self._parent[x]
        return root

    def union(self, a: int, b: int) -> bool:
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self._rank[root_a] < self._rank[root_b]:
            root_a, root_b = root_b, root_a
        self._parent[root_b] = root_a
        if self._rank[root_a] == self._rank[root_b]:
            self._rank[root_a] += 1
        self._sets -= 1
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    @property
    def set_count(self) -> int:
        return self._sets


def main() -> None:
    dsu = DisjointSet(6)
    for a, b in ((0, 1), (1, 2), (3, 4)):
        dsu.union(a, b)
    print("0 и 2 связаны:", dsu.connected(0, 2))
    print("0 и 3 связаны:", dsu.connected(0, 3))
    print("Количество множеств:", dsu.set_count)


if __name__ == "__main__":
    main()
