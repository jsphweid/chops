"""
===== Initial Thoughts =====
maybe sort
58
[34,23,1,24,75,33,54,8] k=60
[1,8,23,24,33,34,54,75]

[1,8,23,24,33,34,54,75] k=60
l=0, r=7, a=76, winner=None
l=0, r=6, a=55, winner=55
l=1, r=6, a=62, winner=55
l=1, r=5, a=42, winner=55
l=2, r=5, a=57, winner=57
l=3, r=5, a=58, winner=58
l=4, r=5, a=67, winner=58
l=4, r=4

[10,20,30] k = 15

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        winner = None
        l, r = 0, len(nums) - 1
        while l < r:
            a = nums[l] + nums[r]
            if a < k:
                winner = max(a, winner) if winner else a
                l += 1
            else:
                r -= 1
        return winner if winner else -1