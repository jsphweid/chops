"""
~~Complexity Analysis
Time - 
Space - 

[[0,1],[1,2],[2,0]]
0, 2
{
    0: [1,2]
    1: [0,2]
    2: [0,1]
}
seen = [0,1,2]
2
"""
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        queue, seen = [start], set()
        while queue:
            node = queue.pop()
            if node in seen:
                continue
            seen.add(node)
            if node == end:
                return True
            for child in adj[node]:
                if child not in seen:
                    queue.append(child)

        return False