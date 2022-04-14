class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        curr = 0
        for num in nums:
            curr ^= num
        return curr