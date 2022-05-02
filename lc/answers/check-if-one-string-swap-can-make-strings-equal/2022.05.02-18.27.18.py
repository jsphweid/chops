"""
s1 = "bank", s2 = "kanb"
bank
sank

diff must be 0 or two
"""
from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1_counts, s2_counts = Counter(s1), Counter(s2)
        for char, count in s1_counts.items():
            if s2_counts[char] != count:
                return False
        diffs = 0
        for l, r in zip(s1, s2):
            if l != r:
                diffs += 1
        return diffs == 0 or diffs == 2
