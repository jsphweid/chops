"""
===== Initial Thoughts =====
brute force you could insert into a sorted list which is O(n)
median is simple from that

=== Brute Force Approach ===
from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.lst = SortedList([])

    def addNum(self, num: int) -> None:
        self.lst.add(num)

    def findMedian(self) -> float:
        N = len(self.lst)
        if N == 1:
            return self.lst[0]
        if N & 1:
            return self.lst[N // 2]
        return (self.lst[N // 2] + self.lst[(N // 2) - 1]) / 2

=== Implemented Approach ===
use two heaps

~~Complexity Analysis
Time - 
Space - 
"""
import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.count = 0

    def addNum(self, num: int):
        self.count += 1
        if len(self.max_heap) == 0:
            heapq.heappush(self.max_heap, -num)
        elif len(self.min_heap) == len(self.max_heap):  # add to max
            if num < self.min_heap[0]:  # and fits
                heapq.heappush(self.max_heap, -num)
            else:
                other = heapq.heappushpop(self.min_heap, num)
                heapq.heappush(self.max_heap, -other)
        else:  # add to min
            if num > -self.max_heap[0]:  # and fits
                heapq.heappush(self.min_heap, num)
            else:
                other = -heapq.heappushpop(self.max_heap, -num)
                heapq.heappush(self.min_heap, other)


    def findMedian(self):
        if self.count % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return -self.max_heap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()