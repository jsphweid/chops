"""
after swap, increment both

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == 0:
                while r < len(nums) and nums[r] == 0: r += 1
                if r == len(nums): break
                nums[l] = nums[r]
                nums[r] = 0
            l += 1
            r += 1
