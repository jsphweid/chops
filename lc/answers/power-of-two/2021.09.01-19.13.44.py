"""
cache answers...
"""

nums = set([2**i for i in range(32)])

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n in nums