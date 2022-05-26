"""
let's try a 2 pointer solution

wrote this but then realized it's not sorted 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l, r]
            if s > target:
                r -= 1
            else:
                l += 1
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment], i]
            seen[num] = i

        # no return because there should always be a solution as defined in the problem