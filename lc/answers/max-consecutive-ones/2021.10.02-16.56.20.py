class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        largest = 0
        streak = 0
        for num in nums:
            if num:
                streak += 1
            else:
                largest = max(largest, streak)
                streak = 0
        return max(largest, streak)