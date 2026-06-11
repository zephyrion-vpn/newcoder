import sys


class WithDict:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z


class WithSlots:
    __slots__ = ("x", "y", "z")

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z


def measure_with_dict(count: int) -> tuple[int, int]:
    instances = [WithDict(i, i, i) for i in range(count)]
    sample = instances[0]
    per_instance = sys.getsizeof(sample) + sys.getsizeof(sample.__dict__)
    return per_instance, per_instance * count


def measure_with_slots(count: int) -> tuple[int, int]:
    instances = [WithSlots(i, i, i) for i in range(count)]
    per_instance = sys.getsizeof(instances[0])
    return per_instance, per_instance * count


def main() -> None:
    count = 100_000
    dict_per, dict_total = measure_with_dict(count)
    slots_per, slots_total = measure_with_slots(count)
    print(f"__dict__:  {dict_per} байт/экз. -> {dict_total / 1024 / 1024:.2f} МБ")
    print(f"__slots__: {slots_per} байт/экз. -> {slots_total / 1024 / 1024:.2f} МБ")
    print(f"Экономия: {(1 - slots_total / dict_total) * 100:.1f}%")


if __name__ == "__main__":
    main()
