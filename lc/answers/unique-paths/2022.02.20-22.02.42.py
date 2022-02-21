"""
recurse(3, 3)
    recurse(2, 3)
        recurse(1, 3) -> 0
        recurse(1, 2)
            recurse(1, 1) -> 1
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
        return matrix[0][0]