"""
===== Initial Thoughts =====
I can't think of any other way except the brute force (tree, changing 1 row at a time)

After reading the hints, seems like another brute force would be to swap every combination of columns.
Then swap every combination of rows after column swap step.
That seems like an aweful lot of work though.

The question is all about insight and I failed to 'get' it. 
"""

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        top = grid[0]
        top_flipped = [1 - n for n in grid[0]]
        for i in range(1, M):
            row = grid[i]
            if row != top and row != top_flipped:
                return False
        return True