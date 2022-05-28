"""
===== Initial Thoughts =====
[-2,1,-3,4,-1,2,1,-5,4]
[0,-2,-1,-4,0,-1,1,2,-3,1]

[5,4,-1,7,8]
[0,5,9,8,15,23]
lowest=0
best=23

[1]
[0,1]
lowest=0
best=1

FAILED ON [-1]
[0,-1]
lowest shouldn't start at 0

FAILED On [5,4,-1,7,8]
[0,5,9,8,15,23]
lowest=5
best=5

[-1,-2,-4]
[0,-1,-3,-7]
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        diffs = [0]
        for num in nums:
            diffs.append(num + diffs[-1])

        lowest = 0
        best = -float("inf")
        for i in range(1, len(diffs)):
            best = max(best, diffs[i] - lowest)
            lowest = min(lowest, diffs[i])
        return best
