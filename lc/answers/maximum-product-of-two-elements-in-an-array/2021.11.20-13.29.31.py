"""
[9,2,3,5,2,6,9,7,9,4,5,5,10,8,9]

9,5

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a, b = nums[0:2]
        small, large = (a, b) if a < b else (b, a)
        for i in range(2, len(nums)):
            if nums[i] > small:
                if nums[i] > large:
                    small, large = large, nums[i]
                else:
                    small = nums[i]
        return (small - 1) * (large - 1)