"""
===== Initial Thoughts =====
just sink the ones on the edges and count the rest
"""

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def sink(i, j):
            if 0 <= i < M and 0 <= j < N and grid[i][j] == 1:
                grid[i][j] = 0  # sink!
                for ii, jj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    sink(i + ii, j + jj)

        for i in range(M):
            sink(i, 0)
            sink(i, N - 1)

        for j in range(N):
            sink(0, j)
            sink(M - 1, j)

        num_left = 0
        for i in range(M):
            for j in range(N):
                num_left += grid[i][j]
        return num_left
