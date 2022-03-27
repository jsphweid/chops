"""
let's try this with indices instead of whole words...
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def recurse(i, j):
            if i < 0 and j < 0:
                return 0
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if word1[i] == word2[j]:
                return recurse(i - 1, j - 1)
            add = 1 + recurse(i, j - 1)
            delete = 1 + recurse(i - 1, j)
            update = 1 + recurse(i - 1, j - 1)
            return min(add, delete, update)

        return recurse(len(word1) - 1, len(word2) - 1)