"""
[3,6,7,11], h = 8
l=1 r=27 m=14 hours=4
l=1 r=14 m=7 hours=5
l=1 r=7 m=4 hours=8
l=1 r=4 m=2 hours=15
l=3 r=4 m=3 hours=10
l=4 r=4 return 4
"""

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, sum(piles)
        while left < right:
            mid = (left + right) // 2
            hours = sum([math.ceil(n / mid) for n in piles])
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left