"""
ops=3
prev=2
[1,1,1]
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr <= prev:
                ops += prev + 1 - curr
                prev += 1
            else:
                prev = curr
        return ops
