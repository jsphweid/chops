from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = Counter()
        for word in words:
            counts.update(word)
        N = len(words)
        for val in counts.values():
            if val % N != 0:
                return False
        return True