from typing import Any, Hashable


class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key: Hashable = None, value: Any = None) -> None:
        self.key = key
        self.value = value
        self.prev: _Node | None = None
        self.next: _Node | None = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Емкость должна быть положительной.")
        self._capacity = capacity
        self._map: dict[Hashable, _Node] = {}
        self._head = _Node()
        self._tail = _Node()
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node: _Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _push_front(self, node: _Node) -> None:
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node
        self._head.next = node

    def get(self, key: Hashable, default: Any = None) -> Any:
        node = self._map.get(key)
        if node is None:
            return default
        self._remove(node)
        self._push_front(node)
        return node.value

    def put(self, key: Hashable, value: Any) -> None:
        node = self._map.get(key)
        if node is not None:
            node.value = value
            self._remove(node)
            self._push_front(node)
            return
        if len(self._map) >= self._capacity:
            lru = self._tail.prev
            self._remove(lru)
            del self._map[lru.key]
        node = _Node(key, value)
        self._map[key] = node
        self._push_front(node)

    def __len__(self) -> int:
        return len(self._map)

    def __contains__(self, key: Hashable) -> bool:
        return key in self._map


def main() -> None:
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)
    print("get a:", cache.get("a"))
    cache.put("c", 3)
    print("get b:", cache.get("b"))
    print("get c:", cache.get("c"))
    print("size:", len(cache))


if __name__ == "__main__":
    main()
