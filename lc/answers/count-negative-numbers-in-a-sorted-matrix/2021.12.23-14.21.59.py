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

first
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

just realized it's sorted vertically too... therefore the m+n makes more sense

[  4,  3,  2, -1],
[  3,  2,  1, -1],
[  1,  1, -1, -2],
[ -1, -1, -2, -3]

i=2, j=0

[3,2],
[1,0]

"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        positives, M, N = 0, len(grid), len(grid[0])
        # do binary search to find first negative on first row
        l, r = 0, N - 1
        row = grid[0]
        while l < r:
            mid = (l + r) // 2
            if row[mid] < 0:
                r = mid
            else:
                l = mid + 1
        i, j = 0, l - 1 if row[l] < 0 else l
        while i < M and j > -1:
            if grid[i][j] < 0:
                positives += i
                j -= 1
            else:
                i += 1
        positives += ((j + 1) * M)
        return (M * N) - positives
