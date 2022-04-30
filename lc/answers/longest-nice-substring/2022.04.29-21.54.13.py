"""
=== Brute Force Approach ===
seems hard to imagine doing this in linear time. But n^2 seems reasonable


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        best = ""
        for i in range(len(s) - 1):
            for j in range(i + 2, len(s) + 1):
                if j - i > len(best):
                    substring = s[i:j]
                    if self.is_good(substring):
                        best = substring
        return best

    def is_good(self, substring):
        s = set(substring)
        for char in s:
            if char.upper() not in s or char.lower() not in s:
                return False
        return True