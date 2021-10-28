class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        abs_k = abs(k)
        min_num_adjusted = min(nums) + abs_k
        max_num_adjusted = max(nums) - abs_k
        return max_num_adjusted - min(min_num_adjusted, max_num_adjusted)