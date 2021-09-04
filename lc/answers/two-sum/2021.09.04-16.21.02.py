"""
brute force solution here is to create two pointers -- a loop inside a loop that iterate over
every possible unique combination (without duplicates).

I can implement a more efficient version in the next answer.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]