class BitSet:
    def __init__(self) -> None:
        self._mask = 0

    def add(self, value: int) -> None:
        self._check(value)
        self._mask |= 1 << value

    def discard(self, value: int) -> None:
        self._check(value)
        self._mask &= ~(1 << value)

    def contains(self, value: int) -> bool:
        self._check(value)
        return bool(self._mask & (1 << value))

    def union(self, other: "BitSet") -> "BitSet":
        return self._wrap(self._mask | other._mask)

    def intersection(self, other: "BitSet") -> "BitSet":
        return self._wrap(self._mask & other._mask)

    def difference(self, other: "BitSet") -> "BitSet":
        return self._wrap(self._mask & ~other._mask)

    def __len__(self) -> int:
        return self._mask.bit_count()

    def __iter__(self):
        mask = self._mask
        while mask:
            low = mask & -mask
            yield low.bit_length() - 1
            mask ^= low

    def __repr__(self) -> str:
        return "{" + ", ".join(str(value) for value in self) + "}"

    @staticmethod
    def _check(value: int) -> None:
        if not 0 <= value <= 63:
            raise ValueError("Допустимы только числа 0..63")

    @classmethod
    def _wrap(cls, mask: int) -> "BitSet":
        result = cls()
        result._mask = mask
        return result


def main() -> None:
    a = BitSet()
    for value in (1, 5, 10, 63):
        a.add(value)
    b = BitSet()
    for value in (5, 10, 20):
        b.add(value)
    print("A:", a)
    print("B:", b)
    print("Объединение:", a.union(b))
    print("Пересечение:", a.intersection(b))
    print("Разность:", a.difference(b))
    print("63 в A?", a.contains(63))


if __name__ == "__main__":
    main()
