"""
=== Implemented Approach ===
using a pqueue

~~Complexity Analysis
Time - O(nlogk)
Space - O(k)

k=3

distances 1 2 2 3 4 6
-2 -2 -1
"""
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        # since the order doesn't matter
        return [(x, y) for (_, x, y) in heap]
