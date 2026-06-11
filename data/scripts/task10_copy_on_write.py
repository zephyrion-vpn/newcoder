from typing import Iterator


class CowList:
    def __init__(self, data: list | None = None) -> None:
        self._data: list = list(data) if data is not None else []
        self._shared = False

    @classmethod
    def _share(cls, data: list) -> "CowList":
        clone = cls.__new__(cls)
        clone._data = data
        clone._shared = True
        return clone

    def copy(self) -> "CowList":
        self._shared = True
        return CowList._share(self._data)

    def _ensure_owned(self) -> None:
        if self._shared:
            self._data = list(self._data)
            self._shared = False

    def append(self, value: object) -> None:
        self._ensure_owned()
        self._data.append(value)

    def __setitem__(self, index: int, value: object) -> None:
        self._ensure_owned()
        self._data[index] = value

    def __getitem__(self, index: int) -> object:
        return self._data[index]

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator:
        return iter(self._data)

    def __repr__(self) -> str:
        return f"CowList({self._data})"

    def buffer_id(self) -> int:
        return id(self._data)


def main() -> None:
    original = CowList([1, 2, 3])
    clone = original.copy()
    print("Общий буфер после copy():", original.buffer_id() == clone.buffer_id())
    clone.append(4)
    print("После записи в клон:")
    print("  original:", original)
    print("  clone:   ", clone)
    print("Буфер разделился:", original.buffer_id() != clone.buffer_id())


if __name__ == "__main__":
    main()
