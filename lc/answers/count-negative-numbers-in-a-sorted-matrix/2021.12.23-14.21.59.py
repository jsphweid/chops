"""
===== Initial Thoughts =====


=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

2 1 0 -1 -2
0 4 m=2
3 4 m=3
3 3

3 2
0 1 0
1 1
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res, N = 0, len(grid[0])
        for row in grid:
            l, r = 0, N - 1
            while l < r:
                mid = (l + r) // 2
                if row[mid] < 0:
                    r = mid
                else:
                    l = mid + 1
            res += 0 if row[l] >= 0 else N - l
        return res