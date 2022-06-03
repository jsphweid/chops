import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        connected = set()
        unconnected = set([(x, y) for x, y in points])
        x, y = points.pop()
        queue = [(0, x, y)]
        total = 0
        while queue:
            dist, x, y = heapq.heappop(queue)
            if (x, y) in connected:
                continue
            connected.add((x, y))
            unconnected.remove((x, y))
            total += dist
            if len(connected) == len(points) + 1:
                return total
            for xx, yy in unconnected:
                d = abs(x - xx) + abs(y - yy)
                heapq.heappush(queue, (d, xx, yy))
