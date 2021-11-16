from math import inf
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        curr = 0
        distances = [inf] * len(points)
        seen = set()
        total = 0
        for _ in range(len(points) - 1):
            seen.add(curr)
            x0, y0 = points[curr]
            next_node = (inf, 0)  # 0 doesn't matter
            for j, (x1, y1) in enumerate(points):
                if j not in seen:
                    distance = abs(x0 - x1) + abs(y0 - y1)
                    distances[j] = min(distances[j], distance)
                    next_node = min(next_node, (distances[j], j))
            cost, node = next_node
            total += cost
            distances[curr] = inf
            curr = node
        return total



