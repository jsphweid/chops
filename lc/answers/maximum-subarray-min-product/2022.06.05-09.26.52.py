"""
===== Initial Thoughts =====
Input: nums = [1,2,3,2]
Output: 14

we want to increase the minimum but also increase sum

Input: nums = [2,3,3,1,2]
Output: 18

Input: nums = [3,1,5,6,4,2]
Output: 60

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
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = -float("inf")
        N = len(nums)
        for i in range(N):
            total = 0
            minimum = float("inf")
            for j in range(i, N):
                minimum = min(minimum, nums[j])
                total += nums[j]
                res = max(res, minimum * total)
        return res % ((10**9) + 7)
