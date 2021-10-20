class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        streak = 1
        winner = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                streak += 1
            else:
                winner = max(winner, streak)
                streak = 1
        return max(winner, streak)
