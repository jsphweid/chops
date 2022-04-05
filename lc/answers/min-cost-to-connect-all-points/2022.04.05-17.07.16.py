"""
I wanted to try prim's using a priority queue

        if len(points) < 2: return 0
        pq = []
        for i in range(len(points) - 1):
            x, y = points[i]
            for j in range(i + 1, len(points)):
                xx, yy = points[j]
                cost = abs(x - xx) + abs(y - yy)
                pq.append((cost, x, y, xx, yy))
        heapq.heapify(pq)
        seen = set()
        res = 0
        while len(seen) < len(points):
            cost, x, y, xx, yy = heapq.heappop(pq)
            if (x, y) in seen and (xx, yy) in seen:
                continue
            seen.add((x, y))
            seen.add((xx, yy))
            res += cost
        return res

fails on [[2,-3],[-17,-8],[13,8],[-17,-15]]
and now it's obvious -- there's no incentive to connect two subgraphs
with my approach. That's why prim's alg is to go from point to point
instead greedily picking the minimum cost along the way
"""
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2: return 0
        unseen = set([tuple(p) for p in points])
        curr = tuple(points[0])
        unseen.remove(curr)
        pq = [(abs(curr[0] - x) + abs(curr[1] - y), x, y) for x, y in unseen]
        heapq.heapify(pq)
        res = 0
        while unseen:
            cost, x, y = heapq.heappop(pq)
            if (x, y) not in unseen:
                continue
            res += cost
            unseen.remove((x, y))
            for xx, yy in unseen:
                cost = abs(x - xx) + abs(y - yy)
                heapq.heappush(pq, (cost, xx, yy))
        return res
