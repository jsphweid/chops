"""
===== Initial Thoughts =====
sort is real easy I think

[3,1,6,3,8,9,2,3,4,6,8,3,1]

[1,1,2,3,3,3,3,4,6,6,8,8,9]

3,1,2,3,1
"""
import heapq
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        heapq.heapify(weight)
        count = 0
        total = 0
        while weight:
            nxt = heapq.heappop(weight)
            if total + nxt > 5000: break
            count += 1
            total += nxt
        return count