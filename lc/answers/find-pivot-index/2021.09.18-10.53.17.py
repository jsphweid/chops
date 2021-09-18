"""
seems pretty straight forward -- we'll get the initial sum. Then we'll scan from left to right subtracting
the sum from the right num. If we move over again, we'll put that num in the left, and take out another num
on the right, placing it in that holding area again. We'll compare sums and if they are equal, we'll return
that index

tracing
[2 1 -1]
right = 2
left = 0
holding = None

holding = 2
right 0
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        holding = None
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            if holding != None:
                left += holding
            holding = nums[i]
            right -= holding
            if left == right:
                return i
        return -1