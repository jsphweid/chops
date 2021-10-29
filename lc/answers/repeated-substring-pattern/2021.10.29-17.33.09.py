"""
===== Initial Thoughts =====
what if we found unique factor pairs and drastically reduced the search space
i.e. str of length 27
i.e. 3x9, 1*27
then we only check those... i.e. 1, 3, 9 (not 27, obviously, since that'd make i
always true)

But that just seems like a lot of work finding factors... is that worth 

~~Complexity Analysis
Time - no idea
Space - 
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        factors = []
        for i in range(1, len(s) // 2 + 1):
            if len(s) % i == 0 and i != len(s): factors.append(i)
        for factor in factors:
            if s[:factor] * (len(s) // factor) == s:
                return True
        return False