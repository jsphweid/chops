"""
failed on [[2,1,1],[2,3,1],[3,4,1]] 4 2
{2:[(1,1),(3,1)],3:[(4,1)]}
dp = [0, inf, inf, inf, inf]
dfs(2)
    
"""
from collections import defaultdict
from math import inf
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for start, end, cost in times:
            adj[start].append((end, cost))
        dp = [0] + [inf] * n

        def dfs(node, total_cost=0):
           if total_cost < dp[node]:
                dp[node] = total_cost
                for nxt, cost in adj[node]:
                    dfs(nxt, total_cost + cost)

        dfs(k)
        res = max(dp)
        return -1 if res == inf else res

