"""
DFS with cache... TLEs...

    def minPathSum(self, grid: List[List[int]]) -> int:
        queue, cache, res = [(0, 0, grid[0][0])], {}, inf
        M, N = len(grid), len(grid[0])
        while queue:
            i, j, total = queue.pop()
            if i == M - 1 and j == N - 1:
                res = min(res, total)
            else:
                if (i, j) in cache and cache[(i, j)] <= total:
                    # not worth exploring...
                    continue

                # add to cache
                cache[(i, j)] = total

                # explore down and right, if possible
                nxt_points = []
                if i != M - 1: nxt_points.append((i + 1, j))
                if j != N - 1: nxt_points.append((i, j + 1))
                for nxt_i, nxt_j in nxt_points:
                    queue.append((nxt_i, nxt_j, total + grid[nxt_i][nxt_j]))
        return res

probably should use dijkstra
(sum, i, j)


import heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        queue, seen = [(grid[0][0], 0, 0)], set()
        M, N = len(grid), len(grid[0])
        while queue:
            total, i, j = heapq.heappop(queue)
            if i == M - 1 and j == N - 1:
                return total
            if (i, j) not in seen:
                seen.add((i, j))

                nxt_points = []
                if i != M - 1: nxt_points.append((i + 1, j))
                if j != N - 1: nxt_points.append((i, j + 1))
                for nxt_i, nxt_j in nxt_points:
                    heapq.heappush(queue, (total + grid[nxt_i][nxt_j], nxt_i, nxt_j))
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if i == M - 1 and j != N - 1:
                    # last row and not right corner
                    grid[i][j] += grid[i][j + 1]
                elif i != M - 1 and j == N - 1:
                    # not last row but right column
                    grid[i][j] += grid[i + 1][j]
                elif i != M - 1:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]





