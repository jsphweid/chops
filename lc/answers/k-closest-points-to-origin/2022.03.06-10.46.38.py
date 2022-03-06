"""
=== Implemented Approach ===
using a pqueue

~~Complexity Analysis
Time - O(klogn)
Space - O(n + k)
"""
import heapq
import math

def get_dist(point: List[int]) -> float:
    # a^2 + b^2 = c^2
    # c = sqrt(a^2 + b^2)
    x, y = point
    return math.sqrt((point[0] ** 2) + (point[1] ** 2))


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(get_dist(p), p) for p in points]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res