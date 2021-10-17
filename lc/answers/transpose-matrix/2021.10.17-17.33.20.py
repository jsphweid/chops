"""
===== Initial Thoughts =====
[[1,2,3],[4,5,6]]

0,0 -> 0,0
0,1 -> 1,0
0,2 -> 2,0
1,0 -> 0,1
1,1 -> 1,1
1,2 -> 2,1
2,0 -> 0,2
2,1 -> 1,2
2,2 -> 2,2
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        ret = [[0] * num_rows for _ in range(num_cols)]
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                ret[j][i] = val
        return ret