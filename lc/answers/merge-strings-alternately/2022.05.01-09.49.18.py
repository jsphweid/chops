"""
word1 = "abcd", word2 = "pq"
i=2 j=2
merged['a', 'p', 'b', 'q']
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        M, N = len(word1), len(word2)
        i = j = 0
        merged = []
        left = True
        while i < M and j < N:
            if left:
                merged.append(word1[i])
                i += 1
            else:
                merged.append(word2[j])
                j += 1
            left = not left
        merged += list(word1[i:]) if i < M else list(word2[j:])
        return "".join(merged)