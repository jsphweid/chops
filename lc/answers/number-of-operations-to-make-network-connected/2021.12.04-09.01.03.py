from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) + 1 < n: return -1
        adj = defaultdict(list)
        for l, r in connections:
            adj[l].append(r)
            adj[r].append(l)

        seen = set()
        def dfs(node):
            if node in seen: return 1
            seen.add(node)
            for nxt in adj[node]:
                if nxt not in seen:
                    dfs(nxt)

        res = n
        for i in range(n):
            res -= dfs(i) or 0
        return res - 1