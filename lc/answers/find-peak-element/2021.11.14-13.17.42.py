"""
nums=[1,2,3,1]
0,3 m=1
2,3 m=2

nums=[1,2,1,3,5,6,4]
0,6 m=3
4,6 m=5

nums=[3,2]
0,1 m=0

nums=[2,3]
0,1 m=0
1,1

nums[4,3,2]
0,2 m=1
0,1 m=0

nums[2,3,4]
0,2 m=1
2,2

[1,2,3,1]
0,3 m=1

"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if mid > 0 and mid < (len(nums) - 1):
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid-1] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            elif mid == 0:
                if nums[mid+1] < nums[0]:
                    return 0
                else:
                    l = 1
        return l
        
                    