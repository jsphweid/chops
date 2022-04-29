"""
===== Initial Thoughts =====
This seems like a fun problem

Looks like the ball can be either above or below the line.

We can view it as always being on top though as well as long as we move
only in diagonals.

Basically a ball exists in a section. It wants to flow left or right based on
the diag. Whether it CAN or not depends on a neighboring diag (which depends on
the direction current diagonal). If relevant neighbor is a wall, then it won't work.
If neighbor is opposite, it won't work.
"""

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        M, N = len(grid), len(grid[0])
        def find_bottom(i, j):
            if i == M:
                return j

            curr = grid[i][j]

            # stuck in a wall
            if curr == 1 and j == N - 1:
                return -1
            if curr == -1 and j == 0:
                return -1
            
            # neighbor not compatible
            if curr == 1 and grid[i][j + 1] == -1:
                return -1
            if curr == -1 and grid[i][j - 1] == 1:
                return -1

            return find_bottom(i + 1, j + curr)

        return [find_bottom(0, j) for j in range(N)]