class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallest = (float("inf"), -1)
        for i, (xx, yy) in enumerate(points):
            if x == xx or y == yy:
                distance = abs(x - xx) + abs(y - yy)
                smallest = min(smallest, (distance, i))
        return smallest[1]