"""
tracing [[0,0],[2,2],[3,10],[5,2],[7,0]]
cost=0 cheapest=[inf, inf, inf, inf, inf] current=0 seen={}
seen={0}
"""


from math import inf
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = 0
        cheapest = [inf] * len(points)
        current = 0
        seen = set()

        for _ in range(len(points) - 1):
            seen.add(current)
            nxt_i = None
            nxt = inf
            for i in range(len(points)):
                if i not in seen:
                    x0, y0 = points[current]
                    x1, y1 = points[i]
                    cheapest[i] = min(cheapest[i], abs(x1 - x0) + abs(y1 - y0))
                    if cheapest[i] < nxt:
                        nxt = cheapest[i]
                        nxt_i = i

            cost += nxt
            cheapest[current] = inf
            current = nxt_i

        return cost
