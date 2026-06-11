class SegmentTree:
    def __init__(self, data: list[int]) -> None:
        if not data:
            raise ValueError("Дерево отрезков нельзя построить из пустого массива.")
        self._n = len(data)
        self._tree = [0] * (2 * self._n)
        self._tree[self._n :] = data
        for i in range(self._n - 1, 0, -1):
            self._tree[i] = self._tree[2 * i] + self._tree[2 * i + 1]

    def update(self, index: int, value: int) -> None:
        if not 0 <= index < self._n:
            raise IndexError("Индекс вне диапазона.")
        i = index + self._n
        self._tree[i] = value
        i >>= 1
        while i:
            self._tree[i] = self._tree[2 * i] + self._tree[2 * i + 1]
            i >>= 1

    def query(self, left: int, right: int) -> int:
        if not 0 <= left <= right <= self._n:
            raise IndexError("Некорректный отрезок [left, right).")
        result = 0
        l, r = left + self._n, right + self._n
        while l < r:
            if l & 1:
                result += self._tree[l]
                l += 1
            if r & 1:
                r -= 1
                result += self._tree[r]
            l >>= 1
            r >>= 1
        return result


def main() -> None:
    tree = SegmentTree([2, 1, 5, 3, 4, 7, 6])
    print("sum[1, 5):", tree.query(1, 5))
    tree.update(2, 10)
    print("после update(2, 10), sum[1, 5):", tree.query(1, 5))
    print("sum[0, 7):", tree.query(0, 7))


if __name__ == "__main__":
    main()
