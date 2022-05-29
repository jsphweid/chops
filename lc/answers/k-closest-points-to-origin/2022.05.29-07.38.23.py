"""
===== Initial Thoughts =====
just use a heap

import heapq
def get_dist(x, y):
    return (x**2 + y**2)**0.5

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances_and_points = [(get_dist(x, y), (x, y)) for x, y in points]
        heapq.heapify(distances_and_points)
        closest = []
        for _ in range(k):
            __, (x, y) = heapq.heappop(distances_and_points)
            closest.append([x, y])
        return closest

what about heappushpop to keep heap size down to size k?

FAILED initially because the heap needs to be a max heap then...

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for i, (x, y) in enumerate(points):
            item = (-get_dist(x, y), x, y)
            if i < k:
                heapq.heappush(closest, item)
            else:
                heapq.heappushpop(closest, item)
        return [[x, y] for _, x, y in closest]

what about nsmallest?
"""
import heapq
def get_dist(point):
    return (point[0]**2 + point[1]**2)**0.5

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=get_dist)