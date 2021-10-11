"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Trie:

    def __init__(self):
        self._root = {}

    def insert(self, word: str) -> None:
        current = self._root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[True] = True

    def search(self, word: str) -> bool:
        current = self._root
        for char in word:
            if char not in current: return False
            current = current[char]
        return True in current

    def startsWith(self, prefix: str) -> bool:
        current = self._root
        for char in prefix:
            if char not in current: return False
            current = current[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)