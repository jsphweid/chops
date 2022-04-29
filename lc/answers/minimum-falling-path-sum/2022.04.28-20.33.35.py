class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        for i in range(N - 2, -1, -1):
            for j in range(N):
                val = matrix[i][j]
                smallest = val + matrix[i + 1][j]
                if j > 0:
                    smallest = min(smallest, val + matrix[i + 1][j - 1])
                if j < N - 1:
                    smallest = min(smallest, val + matrix[i + 1][j + 1])
                matrix[i][j] = smallest
        return min(matrix[0])
