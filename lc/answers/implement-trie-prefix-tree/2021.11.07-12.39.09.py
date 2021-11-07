"""
{
    "a": {
        "p": {
            "p": {
                "l": {
                    "e": {
                        "has_end": True
                    }
                }
            }
        }
    }
}
"""

class Trie:

    def __init__(self):
        self._trie = {}

    def insert(self, word: str) -> None:
        node = self._trie
        for char in word:
            if char in node:
                node = node[char]
            else:
                node[char] = {"has_end": False}
                node = node[char]
        node["has_end"] = True

    def search(self, word: str) -> bool:
        node = self._trie
        for char in word:
            if char in node:
                node = node[char]
            else:
                return False
        return node["has_end"]


    def startsWith(self, prefix: str) -> bool:
        node = self._trie
        for char in prefix:
            if char in node:
                node = node[char]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)