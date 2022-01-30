"""
===== Initial Thoughts =====
[-2,1,-3,4,-1,2,1,-5,4]
[-2,-1,-4,0,-1,1,2,-3,1]
-2       1

[5,4,-1,7,8]
[5,9,8,15,23]

[-2,1,-3,4,-1,2,1,-5,4]

Actually this is like that stock problem... trying to find the largest increase.

s=0 smallest=-1 res=-inf
"""
from math import inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, smallest, res = 0, 0, -inf
        for n in nums:
            s += n
            res = max(res, s - smallest)
            smallest = min(smallest, s)
        return res

