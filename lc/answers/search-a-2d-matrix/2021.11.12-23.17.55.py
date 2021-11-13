"""
3x4 (3 rows, 4 columns)
0 - 0,0
1 - 0,1
2 - 0,2
3 - 0,3
4 - 1,0
5 - 1,1
6 - 1,2
7 - 1,3
8 - 2,0
9 - 2,1

1x2
[[3, 4]]
0

[[1]]
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        l, r = 0, (num_rows * num_cols) - 1
        while l < r:
            mid = (l + r) // 2
            i, j = divmod(mid, num_cols)
            val = matrix[i][j]
            if val == target:
                return True
            if val < target:
                l = mid + 1
            else:
                r = mid
        i, j = divmod(l, num_cols)
        return matrix[i][j] == target