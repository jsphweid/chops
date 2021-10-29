class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        d = {0: [], 1: []}
        for n in nums: d[n % 2].append(n)
        res = []
        for i in range(len(nums)):
            res.append(d[i % 2].pop())
        return res
        