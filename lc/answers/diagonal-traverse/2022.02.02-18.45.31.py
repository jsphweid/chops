"""
1 2 3
4 5 6
7 8 9
going down
1, 0
[1,2,4] 2, 0
"""
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        i, j = 0, 0
        M, N = len(mat), len(mat[0])
        going_up = True

        for _ in range(M*N):
            res.append(mat[i][j])

            # set next
            ii, jj = (i-1, j+1) if going_up else (i+1, j-1)
            if 0 <= ii < M and 0 <= jj < N:
                i, j = ii, jj
                continue

            # if going_up could be right or down
            if going_up:
                i, j = (i, j+1) if j+1 < N else (i+1, j)
            else:
                i, j = (i+1, j) if i+1 < M else (i, j+1)
            going_up = not going_up
        return res


"""
1 1
1 1
1 1
1 1
1 1
"""
