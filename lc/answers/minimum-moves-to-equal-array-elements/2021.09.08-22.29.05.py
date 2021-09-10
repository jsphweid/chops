"""
So I played around with this A LOT on paper before seeing what I think is the winning pattern

The idea is to pick the highest and lowest values from the list. Then if you add up all the inner values' distance to the lowest,
it should equal the final number you want.
"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        nums.sort()
        lowest = nums.pop(0)
        highest = nums.pop()

        min_moves = highest - lowest

        for num in nums:
            min_moves += (num - lowest)

        return min_moves