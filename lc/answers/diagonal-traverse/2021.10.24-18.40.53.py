"""
===== Initial Thoughts =====
I whiteboarded this with Brian

3 rows 2 columns

0,0
0,1
1,1
2,1



"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row_length = len(mat[0])
        top = [[0, i] for i in range(row_length - 1)]
        right = [[i, row_length - 1] for i in range(len(mat))]

        def get_down_left(i, j):
            res = []
            while i < len(mat) and j >= 0:
                res.append(mat[i][j])
                i += 1
                j -= 1
            return res

        final = []
        for inc, coord in enumerate(top + right):
            i, j = coord
            diag = get_down_left(i, j)
            final += diag if inc & 1 else diag[::-1]
        return final
