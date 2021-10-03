"""
===== Initial Thoughts =====
I think we can do something like figure out counts of each, then scan through nums in order (ordered dict?)
and find the two that have the highest number. Once we have that information, then we can filter the items
in the array that equal those two numbers

~~Complexity Analysis
Time - O(nlogn) (to sort) + O(3n)
Space - O(3n) (count dict + sorted version of nums)

tracing...

[1,3,2,2,5,2,3,7]
counts = {1: 1, 3: 2, 2: 3, 5: 1, 7: 1}
sorted_nums = [1, 2, 3, 5, 7]

"""
from collections import defaultdict
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for n in nums: counts[n] += 1
        
        sorted_nums = sorted(counts.keys())
        if len(sorted_nums) < 2: return 0
        
        best_total = 0
        for i in range(1, len(sorted_nums)):
            num = sorted_nums[i]
            prev = sorted_nums[i - 1]
            if num - prev == 1:
                best_total = max(best_total, counts[num] + counts[prev])
        return best_total