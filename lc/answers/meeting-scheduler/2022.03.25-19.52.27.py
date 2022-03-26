"""
slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]]
[(0,15),(10,50),(60,120),(60,70),(140,210)]
"""

import heapq
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        lst = [(s, e) for s, e in  slots1 + slots2 if s + duration <= e]
        heapq.heapify(lst)
        while len(lst) > 1:
            top = heapq.heappop(lst)
            other = lst[0]
            if other[0] + duration <= top[1]:
                return [other[0], other[0] + duration]
        return []