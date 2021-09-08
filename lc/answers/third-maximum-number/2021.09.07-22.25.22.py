class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        if len(unique_nums) < 3:
            return max(nums)
        return sorted(unique_nums, reverse=True)[2]