import math
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        distances = [math.inf] * N
        i = 0
        total = 0
        seen = set()

        for _ in range(N - 1):
            x0, y0 = points[i]
            seen.add(i)
            for j, (x1, y1) in enumerate(points):
                if j not in seen:
                    cost = abs(x1 - x0) + abs(y1 - y0)
                    distances[j] = min(cost, distances[j])
            min_distance, next_point_index = min((d, j) for j, d in enumerate(distances))
            distances[next_point_index] = math.inf
            total += min_distance
            i = next_point_index
        return total