import hashlib
import math


class BloomFilter:
    def __init__(self, expected_items: int, false_positive_rate: float = 0.01) -> None:
        if expected_items <= 0:
            raise ValueError("expected_items должно быть положительным.")
        if not 0 < false_positive_rate < 1:
            raise ValueError("false_positive_rate должно быть в (0, 1).")
        self.size = self._optimal_size(expected_items, false_positive_rate)
        self.hash_count = self._optimal_hash_count(self.size, expected_items)
        self.bits = bytearray((self.size + 7) // 8)
        self.count = 0

    @staticmethod
    def _optimal_size(n: int, p: float) -> int:
        return max(1, int(-(n * math.log(p)) / (math.log(2) ** 2)))

    @staticmethod
    def _optimal_hash_count(m: int, n: int) -> int:
        return max(1, round((m / n) * math.log(2)))

    def _hashes(self, item: str):
        data = item.encode("utf-8")
        h1 = int.from_bytes(hashlib.sha256(data).digest()[:8], "big")
        h2 = int.from_bytes(hashlib.md5(data).digest()[:8], "big")
        for i in range(self.hash_count):
            yield (h1 + i * h2) % self.size

    def add(self, item: str) -> None:
        for position in self._hashes(item):
            self.bits[position // 8] |= 1 << (position % 8)
        self.count += 1

    def __contains__(self, item: str) -> bool:
        return all(self.bits[p // 8] & (1 << (p % 8)) for p in self._hashes(item))


def main() -> None:
    bloom = BloomFilter(expected_items=1000, false_positive_rate=0.01)
    present = [f"item-{i}" for i in range(500)]
    for item in present:
        bloom.add(item)
    true_positives = sum(item in bloom for item in present)
    false_positives = sum(f"absent-{i}" in bloom for i in range(5000))
    print(f"Размер битового массива: {bloom.size}, хеш-функций: {bloom.hash_count}")
    print(f"Истинно положительные: {true_positives}/{len(present)} (должно быть 100%)")
    print(f"Ложноположительные: {false_positives}/5000 ({false_positives / 5000:.4f})")


if __name__ == "__main__":
    main()
