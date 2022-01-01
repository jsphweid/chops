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


[[0,1],[0,0]]
dfs(0, 0)
    dfs(1, 0)
        dfs(2, 0)
        dfs(1, 1) -> add 1
    dfs(0, 1)

[[0,1],[0,0]]
dfs([[0,1],[0,0]], 0, 0, {})
    dfs([[0,1],[0,0]], 1, 0, {}) -> 1
        dfs([[0,1],[0,0]], 2, 0, {}) -> 0
        dfs([[0,1],[0,0]], 1, 1, {}) -> 1
        changes memo to {(1,0): 1}
    dfs([[0,1],[0,0]], 0, 1, {}) -> 0
    changes memo to {(1,0): 1, (0, 0): 1}


somehow this doesn't work...

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid, i=0, j=0, memo=dict()):
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        key = (i, j)
        if key in memo: return memo[key]
        if 0 <= i < M and 0 <= j < N and obstacleGrid[i][j] == 0:
            if i == M - 1 and j == N - 1:
                return 1
            else:
                down = self.uniquePathsWithObstacles(obstacleGrid, i + 1, j, memo)
                right = self.uniquePathsWithObstacles(obstacleGrid, i, j + 1, memo)
                memo[key] = down + right
                return memo[key]
        else:
            return 0
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        return self.helper(obstacleGrid, 0, 0, {})

    def helper(self, obstacleGrid, i, j, memo):
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        key = (i, j)
        if key in memo: return memo[key]
        if 0 <= i < M and 0 <= j < N and obstacleGrid[i][j] == 0:
            if i == M - 1 and j == N - 1:
                return 1
            else:
                down = self.helper(obstacleGrid, i + 1, j, memo)
                right = self.helper(obstacleGrid, i, j + 1, memo)
                memo[key] = down + right
                return memo[key]
        else:
            return 0





