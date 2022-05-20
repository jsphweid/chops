class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(M):
            for j in range(N):
                if i == j == 0:
                    obstacleGrid[0][0] = 1
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    above = 0 if i == 0 else obstacleGrid[i - 1][j]
                    left = 0 if j == 0 else obstacleGrid[i][j - 1]
                    obstacleGrid[i][j] += above + left
        return obstacleGrid[M - 1][N - 1]