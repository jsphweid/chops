"""
===== Initial Thoughts =====
let's use a priority queue... this will allow us to only visit each node once
Time - O()
Space - O(n)
"""
from collections import defaultdict
from heapq import heappop, heappush, heapify
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj, t, queue = defaultdict(list), {}, [(0, k)]
        for start, end, time in times:
            adj[start].append((end, time))
        while queue:
            time, node = heappop(queue)
            if node not in t:
                t[node] = time
                for nxt, nxt_time in adj[node]:
                    heappush(queue, (nxt_time + time, nxt))
        return max(t.values()) if len(t) == n else -1
