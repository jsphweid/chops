"""
===== Initial Thoughts =====
just sort then do top 2 minus bottom 2

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2] * nums[-1]) - (nums[0] * nums[1])

~~Complexity Analysis
Time - O(nlog(n))
Space - O(1)

But how do we do the n...?
Well it's trivial to get the largest and smallest
to get kth largest and smallest, we could use quick select although that's a lot of work

[5,6,2,7,4]
min1=inf min2=inf
max1=-inf max2=-inf
"""
from collections import Counter
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1 = min2 = float("inf")
        max1 = max2 = -float("inf")
        for n in nums:
            if n <= min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
            
            if n >= max2:
                max2, max1 = n, max2
            elif n > max1:
                max1 = n
        return (max1 * max2) - (min1 * min2)
