import mmap
import os
import tempfile
import time


def search_mmap(path: str, needle: bytes) -> list[int]:
    positions: list[int] = []
    with open(path, "rb") as handle:
        with mmap.mmap(handle.fileno(), 0, access=mmap.ACCESS_READ) as mapped:
            start = 0
            while True:
                index = mapped.find(needle, start)
                if index == -1:
                    break
                positions.append(index)
                start = index + 1
    return positions


def search_naive(path: str, needle: bytes, chunk_size: int = 1 << 20) -> list[int]:
    positions: list[int] = []
    overlap = len(needle) - 1
    offset = 0
    tail = b""
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            window = tail + chunk
            base = offset - len(tail)
            start = 0
            while True:
                index = window.find(needle, start)
                if index == -1:
                    break
                positions.append(base + index)
                start = index + 1
            tail = window[-overlap:] if overlap > 0 else b""
            offset += len(chunk)
    return positions


def main() -> None:
    path = tempfile.mktemp(suffix=".bin")
    needle = b"NEEDLE_MARKER"
    block = b"x" * (1 << 20)
    try:
        with open(path, "wb") as handle:
            for i in range(64):
                handle.write(block)
                if i in (10, 40):
                    handle.write(needle)
        size_mb = os.path.getsize(path) / 1024 / 1024

        start = time.perf_counter()
        mmap_result = search_mmap(path, needle)
        mmap_time = time.perf_counter() - start

        start = time.perf_counter()
        naive_result = search_naive(path, needle)
        naive_time = time.perf_counter() - start

        print(f"Размер файла: {size_mb:.0f} МБ")
        print(f"mmap:  найдено {len(mmap_result)} за {mmap_time * 1000:.2f} мс")
        print(f"naive: найдено {len(naive_result)} за {naive_time * 1000:.2f} мс")
        print("Позиции совпадают:", mmap_result == naive_result)
    finally:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    main()
