class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in d:
                return [d[compliment], i]
            d[num] = i
        