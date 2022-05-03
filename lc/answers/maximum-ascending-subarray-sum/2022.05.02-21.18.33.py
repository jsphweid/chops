"""
[10,20,30,5,10,50,0]
i=4
curr=65
best=65

FAILS on
[3,6,10,1,8,9,9,8,9]

Needs to be less than or equal to...
Should've tested one with two of the same digit next to each other.
"""

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        nums.append(0)
        curr = best = 0
        for i, num in enumerate(nums):
            if i == 0 or num <= nums[i - 1]:
                best = max(best, curr)
                curr = num
            else:
                curr += num
        return best
