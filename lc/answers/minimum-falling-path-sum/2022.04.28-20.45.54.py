class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)

        @cache
        def find_min(i, j):
            if i == N - 1:
                return matrix[i][j]
            candidates = [find_min(i + 1, j)]
            if j > 0: candidates.append(find_min(i + 1, j - 1))
            if j < N - 1: candidates.append(find_min(i + 1, j + 1))
            return matrix[i][j] + min(candidates)

        return min(find_min(0, j) for j in range(N))