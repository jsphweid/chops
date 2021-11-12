"""
===== Initial Thoughts =====
we know we never have two back to back numbers that are the same
[1,2,1,3,5,6,4]
7 items, 0-6
0->1
3->3
4->5
5->6
6->4

[1,2,1,4,5,6,7,8]
l=1 r=6 m=3 v=4


[1,2,3,4,5,6,7,8]



=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        left = 1
        right = n - 2
        while left <= right:
            # mid = left + ((right - left) // 2)
            mid = (left + right) // 2
            if (nums[mid] > nums[mid - 1]) and (nums[mid] > nums[mid + 1]):
                return mid
            elif nums[mid] < nums[mid - 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
        