from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        num_good = 0
        queue = deque([])
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    queue.append([i, j])
                elif grid[i][j] == 1:
                    num_good += 1
        minute = -1
        if num_good == 0:
            return 0
        while queue:
            minute += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for ii, jj in [[1,0],[0,1],[-1,0],[0,-1]]:
                    ii, jj = i + ii, j + jj
                    if 0 <= ii < M and 0 <= jj < N and grid[ii][jj] == 1:
                        grid[ii][jj] = 2
                        num_good -= 1
                        queue.append([ii, jj])
        return minute if num_good == 0 else -1
