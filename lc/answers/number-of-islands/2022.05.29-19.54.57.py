class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])

        def sink(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                for ii, jj in [[1,0],[0,1],[-1,0],[0,-1]]:
                    ii += i
                    jj += j
                    if 0 <= ii < M and 0 <= jj < N:
                        sink(ii, jj)


        count = 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    count += 1
                    sink(i, j)

        return count