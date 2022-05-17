class Solution:
    def arraySign(self, nums: List[int]) -> int:
        zeros = negatives = 0
        for num in nums:
            if num == 0:
                zeros += 1
            if num < 0:
                negatives += 1
        modifier = 1 if negatives % 2 == 0 else -1
        return 0 if zeros > 0 else modifier