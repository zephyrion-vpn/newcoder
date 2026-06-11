class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, prefix: str) -> "TrieNode | None":
        node = self.root
        for char in prefix:
            node = node.children.get(char)
            if node is None:
                return None
        return node


def main() -> None:
    trie = Trie()
    for word in ["apple", "app", "application"]:
        trie.insert(word)
    print("search('app'):", trie.search("app"))
    print("search('ap'):", trie.search("ap"))
    print("starts_with('app'):", trie.starts_with("app"))
    print("starts_with('xyz'):", trie.starts_with("xyz"))
    print("search('application'):", trie.search("application"))


if __name__ == "__main__":
    main()
