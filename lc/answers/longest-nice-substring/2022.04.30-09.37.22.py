"""
===== Initial Thoughts =====
read about divide and conquer and it made a lot of sense to me

~~Complexity Analysis
Time - O(n^2)
Space - O(n)
"""

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        N = len(s)
        if N < 2: return ""
        chars = set(s)
        for i, char in enumerate(s):
            if char.upper() not in chars or char.lower() not in chars:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right
        return s