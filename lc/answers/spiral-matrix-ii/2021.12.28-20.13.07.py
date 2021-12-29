"""
===== Initial Thoughts =====
generate a path, and then put the numbers in the correct spot following the path
[[1,2,3],[0,0,4],[0,6,5]]
0,0 - 0,1 - 0,2 - 1,2 - 2,2 etc.

[[1,2,3],[4,5,6],[7,8,9]]
    [[1,2,3],[8,9,4],[7,6,5]]

r2 d1 l1
r3 d2 l2 u1 r1
r4 d3 l3 u2 r2 d1 l1
r5 d4 l4 u3 r3 d2 l2 u1 r1

i=5 res=1
i=4 res=2 res=3

1 to n + 1
i=1 


n=2
di=1 do_again=True curr=2
res = [[1,2,3],[0,0,4],[0,0,0]]
point=[1,2]
num=1
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        point = (0, 0)
        di, do_again, curr = 0, False, n
        res = [[0] * n for _ in range(n)]
        for num in range(1, n * n + 1):
            i, j = point
            res[i][j] = num

            curr -= 1

            if not curr:
                if not do_again:
                    n -= 1
                curr = n
                do_again = not do_again
                di += 1
                if di == 4:
                    di = 0

            dir_i, dir_j = directions[di]
            point = (i + dir_i, j + dir_j)

        return res


