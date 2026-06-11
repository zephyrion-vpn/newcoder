import heapq
from collections import Counter


class _Node:
    __slots__ = ("freq", "char", "left", "right")

    def __init__(
        self,
        freq: int,
        char: str | None = None,
        left: "_Node | None" = None,
        right: "_Node | None" = None,
    ) -> None:
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right


def build_huffman_codes(text: str) -> dict[str, str]:
    if not text:
        return {}
    frequencies = Counter(text)
    if len(frequencies) == 1:
        return {next(iter(frequencies)): "0"}

    counter = 0
    heap: list[tuple[int, int, _Node]] = []
    for char, freq in sorted(frequencies.items()):
        heap.append((freq, counter, _Node(freq, char)))
        counter += 1
    heapq.heapify(heap)

    while len(heap) > 1:
        freq_a, _, node_a = heapq.heappop(heap)
        freq_b, _, node_b = heapq.heappop(heap)
        merged = _Node(freq_a + freq_b, None, node_a, node_b)
        heapq.heappush(heap, (merged.freq, counter, merged))
        counter += 1

    codes: dict[str, str] = {}

    def walk(node: _Node, prefix: str) -> None:
        if node.char is not None:
            codes[node.char] = prefix
            return
        walk(node.left, prefix + "0")
        walk(node.right, prefix + "1")

    walk(heap[0][2], "")
    return codes


def encode(text: str, codes: dict[str, str]) -> str:
    return "".join(codes[char] for char in text)


def main() -> None:
    text = "abracadabra"
    codes = build_huffman_codes(text)
    encoded = encode(text, codes)
    print("Таблица кодов:")
    for char, code in sorted(codes.items()):
        print(f"  {char!r}: {code}")
    print(f"Исходный размер: {len(text) * 8} бит")
    print(f"Сжатый размер: {len(encoded)} бит")


if __name__ == "__main__":
    main()
