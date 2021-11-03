class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res, acc = [], 0
        for n in nums:
            acc *= 2
            acc += n
            res.append(acc % 5 == 0)
        return res