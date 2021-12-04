from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for l, r in edges:
            adj[l].append(r)
            adj[r].append(l)
        seen = set()
        def count(node):
            if node in seen: return 1
            seen.add(node)
            for n in adj[node]:
                count(n)
        res = n
        for i in range(n):
            res -= count(i) or 0
        return res