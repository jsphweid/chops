"""
from collections import defaultdict
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        seen = list(range(len(edges) + 1))
        for p, q in edges:
            adj[p].append(q)
            adj[q].append(p)

        def longest(node):
            seen[node] = None
            neighbors = [n for n in adj[node] if seen[n] is not None]
            if not neighbors:
                seen[node] = node
                return 0
            best = 0
            for neighbor in neighbors:
                best = max(best, longest(neighbor))
            seen[node] = node
            return best + 1

        return max([longest(k) for k, v in adj.items() if len(v) == 1])


The problem with my idea is there is lots of repetition.

Read some discussions... Will fix
"""

from collections import defaultdict
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        seen = list(range(len(edges) + 1))
        for p, q in edges:
            adj[p].append(q)
            adj[q].append(p)
        diameter = 0
        seen = set()
        def dfs(node):
            nonlocal diameter
            unseen = [n for n in adj[node] if n not in seen]
            if not unseen:
                return 1
            seen.add(node)
            distances = [dfs(n) for n in unseen]
            distances.sort(reverse=True)
            diameter = max(diameter, sum(distances[:2]))
            return distances[0] + 1
        dfs(0)
        return diameter
