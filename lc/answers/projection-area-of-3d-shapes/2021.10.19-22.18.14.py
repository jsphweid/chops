"""
===== Initial Thoughts =====
should be possible by iterating over each one... we have to look at it three different
ways... from top, we just increment 1. The others we have to store a list
of heights from one angle then the other. We have to get the max of each row. The indexing
here will be a little tricky but it shouldn't be too impossible considering it's a simple
square

~~Complexity Analysis
Time - O(n^2)
Space - O(n^2)?

0,0 - 1
0,1 - 2
1,0 - 3
1,1 - 4
"""

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = 0
        l = len(grid)
        xz = [0] * l
        yz = [0] * l
        for i in range(l):
            for j in range(l):
                curr = grid[i][j]
                top += min(1, curr)
                xz[i] = max(xz[i], curr)
                yz[j] = max(yz[j], curr)
        return sum(xz) + sum(yz) + top