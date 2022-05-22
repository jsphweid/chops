"""
===== Initial Thoughts =====
[4,5,6,7,0,1,2]
 0 1 2 3 4 5 6
         4   6
         4 5
         4

[3,4,5,1,2]
 0 1 2 3 4
       3 4
       3

[6,7,0,1,2,3,4,5]
 0 1 2 3 4 5 6 7
 0     3
     2 3
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
