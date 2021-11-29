"""
===== Initial Thoughts =====
should be possible with 1 pass... just counting 0's / 1's as separate variables really
when they equal each other (and are not 1), then increment a global counter by 1 and
reset those variables to 0

~~Complexity Analysis
Time - O(n)
Space - O(1)

tracing "RLRRRLLRLL"
l=0 r=0 count=2
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r, count = 0, 0, 0
        for char in s:
            if char == "L": l += 1
            if char == "R": r += 1
            if l == r:
                count += 1
                l, r = 0, 0
        return count