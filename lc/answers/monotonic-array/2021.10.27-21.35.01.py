"""
===== Initial Thoughts =====


=== Brute Force Approach ===
sort it twice and assert that the original array = the sorted one or the sorted twice one.

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        arr1 = sorted(nums)
        if nums == arr1: return True
        if nums == sorted(nums, reverse=True): return True
        return False