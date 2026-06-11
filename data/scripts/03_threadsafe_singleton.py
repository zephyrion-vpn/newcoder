import threading


class Singleton:
    _instance: "Singleton | None" = None
    _lock = threading.Lock()

    def __new__(cls) -> "Singleton":
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # double-checked locking
                    instance = super().__new__(cls)
                    instance.value = 0
                    cls._instance = instance
        return cls._instance


def main() -> None:
    instances: list[int] = []
    barrier = threading.Barrier(20)

    def create() -> None:
        barrier.wait()
        instances.append(id(Singleton()))

    threads = [threading.Thread(target=create) for _ in range(20)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f"Создано потоков: {len(instances)}")
    print(f"Уникальных экземпляров: {len(set(instances))} (должно быть 1)")


if __name__ == "__main__":
    main()
