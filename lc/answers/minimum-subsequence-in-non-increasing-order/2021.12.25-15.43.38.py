class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        nums.sort(reverse=True)
        res, left_total = [], 0
        for num in nums:
            left_total += num
            total -= num
            res.append(num)
            if left_total > total:
                break
        return res