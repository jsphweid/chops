"""
===== Initial Thoughts =====
[0,1,0,4,3,2,2,2] val = 2

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
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        if not N: return 0
        i = N - 1
        for j in range(i, -1, -1):
            if nums[j] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i -= 1
        return i + 1
