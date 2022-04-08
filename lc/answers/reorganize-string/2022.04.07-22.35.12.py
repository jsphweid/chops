"""
res = "aba"
"""
import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(pq)
        res = ""
        while pq:
            ncount, char = heapq.heappop(pq)
            if not pq:
                if (res and res[-1] == char) or ncount < -1:
                    return ""
                return res + char
            ncount2, char2 = heapq.heappop(pq)
            res += char + char2
            if ncount < -1: heapq.heappush(pq, (ncount + 1, char))
            if ncount2 < -1: heapq.heappush(pq, (ncount2 + 1, char2))
        return res
