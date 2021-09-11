class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        record = 0
        current_streak = 0
        for num in nums:
            if num == 1:
                current_streak += 1
            else:
                if current_streak:
                    record = max(record, current_streak)
                    current_streak = 0
        return max(record, current_streak)