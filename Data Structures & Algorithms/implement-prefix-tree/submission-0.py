class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def _walk(self, s: str):
        cur = self.root
        for c in s:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None