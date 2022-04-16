"""
=== Brute Force Approach ===
join them and compare

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

~~Complexity Analysis
Time - O(m + n)
Space - O(m + n)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

word1 = ["ab", "c"], word2 = ["a", "bc"]

l, ll, r, rr = 2, 0, 2, 0
"""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l, ll, r, rr = 0, 0, 0, 0
        while True:
            if word1[l][ll] != word2[r][rr]:
                return False
            ll += 1
            rr += 1
            if ll == len(word1[l]):
                l += 1
                ll = 0
            if rr == len(word2[r]):
                r += 1
                rr = 0
            if l == len(word1) or r == len(word2):
                return l == len(word1) and r == len(word2)
