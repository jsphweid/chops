"""
0,0 1,1 2,2
0,2 1,1 2,0
"""

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N, res = len(mat), 0
        for i in range(N):
            res += mat[i][i]
            if i != N - 1 - i:
                res += mat[i][N - 1 - i]
        return res