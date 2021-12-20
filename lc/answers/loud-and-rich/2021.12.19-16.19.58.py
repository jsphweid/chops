"""
num_to_beat, person
dfs(0, 3)
    dfs(2, 2) -> (2, 1)
    dfs(3, 2)
        dfs(5, 2) -> (1, 5)
        dfs(4, 2) -> (2, 1)
"""

from collections import defaultdict
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj = defaultdict(list)
        for u, v in richer:
            adj[v].append(u)
        cache = {}
        def dfs(node):
            if node in cache: return cache[node]
            curr = quiet[node], node
            if not adj[node]: return curr
            best = min([curr] + [dfs(child) for child in adj[node]])
            cache[node] = best
            return best
        res = []
        for i in range(len(quiet)):
            val, node = dfs(i)
            res.append(node if val < quiet[i] else i)
        return res