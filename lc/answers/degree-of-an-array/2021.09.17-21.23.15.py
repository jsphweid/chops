"""
High level = 
1. find num(s) involved in degree
2. find first and last index of each of those num(s)
3. get the difference of each and return the smallest

I think we can do it in one pass if we capture the right info
"""

from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        positions = defaultdict(list)
        for i, num in enumerate(nums):
            counts[num] += 1
            positions[num].append(i)

        # 1. find num(s) involved in degree
        degree = max(counts.values())
        nums_involved = [num for num, count in counts.items() if count == degree]

        # 2. find first and last index of each of those num(s)
        # 3. get the difference of each and return the smallest
        return min(map(lambda n: positions[n][-1] - positions[n][0], nums_involved)) + 1