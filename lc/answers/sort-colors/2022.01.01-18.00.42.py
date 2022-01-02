"""
[0,0,1,1,2,2]
l=2 r=3


[0,1,0,2,1,2,0,0,2,1,2,2,1,2]
l=1 r=12 temp=7


[0,0,0,0,1,1,1,1,2,2,2,2,2,2]
l=4 r=8
i=8


[0,1,0,2,1,2,0,0,2,1,2,2,0,1]

[0,1,2]
l=1 r=1 i=1
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, l, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                tmp = nums[l]
                nums[l] = nums[i]
                nums[i] = tmp
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                tmp = nums[r]
                nums[r] = nums[i]
                nums[i] = tmp
                r -= 1