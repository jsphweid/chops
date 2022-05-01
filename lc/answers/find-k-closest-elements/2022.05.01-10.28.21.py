"""
arr = [1,2,3,4,5], k = 4, x = 3
expected result -> [1,2,3,4]
"""

import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = []
        for num in arr:
            heapq.heappush(q, (abs(num - x), num))
        closest = []
        for _ in range(k):
            closest.append(heapq.heappop(q)[1])
        closest.sort()
        return closest