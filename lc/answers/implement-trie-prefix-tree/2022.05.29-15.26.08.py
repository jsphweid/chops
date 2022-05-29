class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr["*"] = curr["*"] + 1 if "*" in curr else 1

    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if char in curr:
                curr = curr[char]
            else:
                return False
        return "*" in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if char in curr:
                curr = curr[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)