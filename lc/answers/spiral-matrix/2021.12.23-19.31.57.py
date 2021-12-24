"""
===== Initial Thoughts =====
3x3
0 1 2 5 8 7 6 3 4

3x4
0 1 2 3 7 11 10 9 8 4 5 6

I think we just have to use simulation

M = 3
N = 4
right_wall = 3
left_wall = -1
bottom_wall = 3
top_wall = -1
direction (1, 0)
0, 4

1 2 3 4
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        res, direction = [], (0, 1)
        M, N = len(matrix), len(matrix[0])
        top_wall, right_wall, bottom_wall, left_wall = 0, N, M, -1
        for _ in range(M * N):
            res.append(matrix[i][j])
            matrix[i][j] = None
            prev_i, prev_j = i, j
            i, j = direction[0] + i, direction[1] + j
            if j == right_wall and direction == (0, 1):
                direction = (1, 0)
                right_wall -= 1
            elif i == bottom_wall and direction == (1, 0):
                direction = (0, -1)
                bottom_wall -= 1
            elif j == left_wall and direction == (0, -1):
                direction = (-1, 0)
                left_wall += 1
            elif i == top_wall and direction == (-1, 0):
                direction = (0, 1)
                top_wall += 1
            else:
                continue
            i, j = direction[0] + prev_i, direction[1] + prev_j
        return res