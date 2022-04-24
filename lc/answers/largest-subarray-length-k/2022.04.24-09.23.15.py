"""
=== Brute Force Approach ===
stringify every k, then change to int then compare with some max

~~Complexity Analysis
Time - O(k(n-k))
Space - O(k)

=== Implemented Approach ===
go through each index n-k and save the largest number using iteration to keep memory low

~~Complexity Analysis
Time - O(k(n-k))
Space - O(1) (except for result)

[1,4,5,2,3] k=3
winner = 2
i=2
j=0
"""

class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        winner = 0
        for i in range(1, len(nums) - k + 1):
            for j in range(k):
                if nums[i + j] > nums[winner + j]:
                    winner = i
                    break
                elif nums[i + j] < nums[winner + j]:
                    break
        return nums[winner: winner + k]

