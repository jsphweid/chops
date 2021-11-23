"""
===== Initial Thoughts =====
[1,2,4,5,7,9,10]
[1,2][4,5][9,10]

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""
from math import inf
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_abs_diff = inf
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]
            min_abs_diff = min(min_abs_diff, diff)

        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_abs_diff:
                res.append([arr[i - 1], arr[i]])
        return res