from collections import defaultdict, deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        is_valid = lambda i, j: 0 <= i < M and 0 <= j < N and grid[i][j]
        queue, adj, seen, total = deque([]), defaultdict(list), set(), 0
        for i in range(M):
            for j in range(N):
                orange = grid[i][j]
                if orange:
                    total += 1
                    if is_valid(i, j + 1): adj[(i, j)].append((i, j + 1))
                    if is_valid(i, j - 1): adj[(i, j)].append((i, j - 1))
                    if is_valid(i + 1, j): adj[(i, j)].append((i + 1, j))
                    if is_valid(i - 1, j): adj[(i, j)].append((i - 1, j))
                    if orange == 2:
                        seen.add((i, j))
                        queue.append((i, j))
        depth = -1
        if not total: return 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for nxt in adj[node]:
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
        return depth if total == len(seen) else -1
