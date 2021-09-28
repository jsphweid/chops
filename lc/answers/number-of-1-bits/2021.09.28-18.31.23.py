"""
===== Initial Thoughts =====
just right shift while at least 1 bit exists... everytime there is a 1, increment a counter

~~Complexity Analysis
Time - O(n) where n is the number of bits
Space - O(1)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n = n >> 1
        return count