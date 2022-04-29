"""
=== Brute Force Approach ===
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    for k in range(j + 1, N):
                        if grid[i][k] == 1:
                            for l in range(i + 1, M):
                                if grid[l][k] == 1:
                                    res += grid[l][j]
        return res

"""
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res = 0
        for i in range(M - 1):  # vertical iterator 1
            for ii in range(i + 1, M):  # vertical iterator 2
                verticals = 0
                for j in range(N):  # horizontal iterator
                    if grid[i][j] and grid[ii][j]:
                        verticals += 1
                # math that translates num verticals -> num rects
                # 1->0, 2->1, 3->3, 4->6, 5->10, etc.
                res += ((verticals ** 2) - verticals) // 2
        return res





