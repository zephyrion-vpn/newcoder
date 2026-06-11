class FixedBlockAllocator:
    def __init__(self, block_size: int, block_count: int) -> None:
        if block_size <= 0 or block_count <= 0:
            raise ValueError("Размер и количество блоков должны быть положительными")
        self._block_size = block_size
        self._block_count = block_count
        self._buffer = bytearray(block_size * block_count)
        self._free: list[int] = list(range(block_count))

    @property
    def free_blocks(self) -> int:
        return len(self._free)

    def allocate(self) -> int:
        if not self._free:
            raise MemoryError("Нет свободных блоков")
        return self._free.pop()

    def free(self, index: int) -> None:
        self._validate(index)
        if index in self._free:
            raise ValueError("Блок уже освобождён")
        start = index * self._block_size
        self._buffer[start : start + self._block_size] = bytes(self._block_size)
        self._free.append(index)

    def write(self, index: int, data: bytes) -> None:
        self._validate(index)
        if len(data) > self._block_size:
            raise ValueError("Данные не помещаются в блок")
        start = index * self._block_size
        self._buffer[start : start + len(data)] = data

    def read(self, index: int) -> bytes:
        self._validate(index)
        start = index * self._block_size
        return bytes(self._buffer[start : start + self._block_size])

    def _validate(self, index: int) -> None:
        if not 0 <= index < self._block_count:
            raise IndexError("Неверный индекс блока")


def main() -> None:
    allocator = FixedBlockAllocator(block_size=8, block_count=4)
    first = allocator.allocate()
    second = allocator.allocate()
    allocator.write(first, b"hello")
    allocator.write(second, b"world!!!")
    print("Блок 1:", allocator.read(first).rstrip(b"\x00"))
    print("Блок 2:", allocator.read(second))
    print("Свободно блоков:", allocator.free_blocks)
    allocator.free(first)
    print("После освобождения:", allocator.free_blocks)


if __name__ == "__main__":
    main()
