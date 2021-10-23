# position of last, diff, current length
"""
[9,4,7,2,10]
9,4   1,-5
9,7   2,-2
9,2   3,-7
9,10  4, 1
4,7   2, 3
4,2   3,-2
4,10  4, 6
7,2   3,-5
7,10  4, 3
2,10  4, 8

failing on [24,13,1,100,0,94,3,0,3]
"""
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        diffs = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                diff = nums[j] - nums[i]
                previous = diffs.get((i, diff), 0)
                diffs[(j, diff)] = previous + 1 if previous else 2
        return max(diffs.values())