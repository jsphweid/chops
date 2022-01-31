"""
===== Initial Thoughts =====
is this a joke?

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

since we only need one element, we can use a min heap then it's (n-k)logn instead of nlogn

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = None
        for _ in range(len(nums) - k + 1):
            res = heapq.heappop(nums)
        return res


we could do it as a max heap (invert everything) to make it klogn but worst case is no different I don't think.
Also interestingly heapq solution is a lot slower than just using sorted.

A one pass solution would be interesting.

=== Brute Force Approach ===


~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

from sortedcontainers import SortedList
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = SortedList(nums[:k])
        for i in range(k, len(nums)):
            if nums[i] > lst[0]:
                lst.remove(lst[0])
                lst.add(nums[i])
        return lst[0]






