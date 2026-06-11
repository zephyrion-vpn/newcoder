import multiprocessing as mp
from multiprocessing import shared_memory


def worker(shm_name: str, size: int) -> None:
    shm = shared_memory.SharedMemory(name=shm_name)
    try:
        for i in range(size):
            shm.buf[i] = shm.buf[i] * 2
    finally:
        shm.close()


def main() -> None:
    size = 8
    shm = shared_memory.SharedMemory(create=True, size=size)
    try:
        for i in range(size):
            shm.buf[i] = i + 1
        before = list(shm.buf[:size])

        process = mp.Process(target=worker, args=(shm.name, size))
        process.start()
        process.join()

        after = list(shm.buf[:size])
        print(f"До:    {before}")
        print(f"После: {after}")
        print(f"Каждый элемент удвоен: {all(a == b * 2 for a, b in zip(after, before))}")
    finally:
        shm.close()
        shm.unlink()


if __name__ == "__main__":
    main()
