"""
this should be trivial with some basic python. It'll take a bit of thinking to get it down to one-pass though...
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        index_of_max_num = nums.index(max_num)
        nums.pop(index_of_max_num)
        for num in nums:
            if num * 2 > max_num:
                return -1
        return index_of_max_num