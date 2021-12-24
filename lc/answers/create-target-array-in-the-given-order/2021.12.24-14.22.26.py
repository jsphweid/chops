class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for num, i in zip(nums, index):
            res.insert(i, num)
        return res