"""
===== Initial Thoughts =====
arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
[2,2,2,1,4,3,3,9,6,7,19]

arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
[22,28,8,6,17,44]



arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
{
    7: 1,
    19: 1
}
[7,19]
[2,2,2,1,4,3,3,9,6]
[2,1,4,3,9,6]
"""
from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = defaultdict(int)
        for num in arr1: counts[num] += 1
        res = []
        for num in arr2:
            res += [num] * counts[num]
            counts[num] = 0
        rest = []
        for num, count in counts.items():
            if count: rest += [num] * counts[num]
        rest.sort()
        return res + rest