"""
===== Initial Thoughts =====
nums = [5,7,7,8,8,10], target = 8
l=0, r=5, m=2
l=3, r=5, m=4
l=3, r=4, m=3
l=3, r=3
3

l=0, r=5, m=2
l=3, r=5, m=4
l=5, r=5

nums = [5,7,7,8,8], target = 8
l=0, r=4, m=2, v=7
l=3, r=4, m=3, v=8
l=4, r=4

[2,2] target=2
l=0, r=1, m=0, v=2
l=0, r=0 exit... l

l=0, r=1, m=0, v=2
l=1, r=1, 

[5,7,7,8,8,10] target = 8
left_most=3

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums): return [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] != target: return [-1, -1]
        left_most = l

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        right_most = l if (nums[len(nums) - 1] == target) else l - 1
        return [left_most, right_most]
