"""
[105,924,32,968]
"""

def is_increasing(arr):
    return all([r > l for l, r in zip(arr, arr[1:])])

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nums[i+1]:
                opt1 = nums[:i] + nums[i+1:]
                opt2 = nums[:i+1] + nums[i+2:]
                return is_increasing(opt1) or is_increasing(opt2)
        return True
