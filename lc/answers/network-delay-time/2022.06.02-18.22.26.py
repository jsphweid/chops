import heapq
from collections import defaultdict

"""
seen = 2, 1, 3, 4
max=2
[(2,4)]
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        seen = set()
        for p, q, l in times:
            adj[p].append((q, l))
        queue = [(0, k)]
        max_latency = 0
        while queue:
            curr_latency, node = heapq.heappop(queue)
            if node in seen: continue
            seen.add(node)
            max_latency = max(max_latency, curr_latency)
            if len(seen) == n: break
            for child, latency in adj[node]:
                if child not in seen:
                    heapq.heappush(queue, (latency + curr_latency, child))
        return max_latency if n == len(seen) else -1