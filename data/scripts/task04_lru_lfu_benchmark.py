import random
from collections import OrderedDict, defaultdict


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._store: OrderedDict[int, int] = OrderedDict()
        self.hits = 0
        self.misses = 0

    def access(self, key: int) -> None:
        if key in self._store:
            self._store.move_to_end(key)
            self.hits += 1
            return
        self.misses += 1
        self._store[key] = key
        if len(self._store) > self.capacity:
            self._store.popitem(last=False)


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self._store: dict[int, int] = {}
        self._freq: dict[int, int] = defaultdict(int)
        self.hits = 0
        self.misses = 0

    def access(self, key: int) -> None:
        if key in self._store:
            self._freq[key] += 1
            self.hits += 1
            return
        self.misses += 1
        if len(self._store) >= self.capacity:
            victim = min(self._store, key=lambda item: self._freq[item])
            del self._store[victim]
            del self._freq[victim]
        self._store[key] = key
        self._freq[key] += 1


def zipf_keys(count: int, universe: int, skew: float) -> list[int]:
    weights = [1.0 / (rank ** skew) for rank in range(1, universe + 1)]
    population = list(range(universe))
    return random.choices(population, weights=weights, k=count)


def hit_rate(cache: LRUCache | LFUCache) -> float:
    total = cache.hits + cache.misses
    return cache.hits / total if total else 0.0


def main() -> None:
    random.seed(42)
    keys = zipf_keys(count=50_000, universe=2_000, skew=1.2)
    lru = LRUCache(capacity=200)
    lfu = LFUCache(capacity=200)
    for key in keys:
        lru.access(key)
        lfu.access(key)
    print(f"LRU hit-rate: {hit_rate(lru) * 100:.2f}%")
    print(f"LFU hit-rate: {hit_rate(lfu) * 100:.2f}%")


if __name__ == "__main__":
    main()
