"""
===== Initial Thoughts =====
I think the longest uncommon subsequence is literally the length of the longest string... unless they are equal, in
which case the answer is -1
"""

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b: return -1
        return max(len(a), len(b))