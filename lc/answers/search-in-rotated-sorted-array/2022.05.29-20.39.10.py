"""
===== Initial Thoughts =====
nums = [4,5,6,7,0,1,2], target = 0
        0 1 2 3 4 5 6
                4 5
                4

nums = [4,5,6,7,0,1,2], target = 3
                4   6
                    6

nums = [1], target = 0

FAILED On [3,1]
           0 1
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:  # left range is valid
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:  # right range is valid
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return l if nums[l] == target else -1
