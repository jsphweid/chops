"""
===== Initial Thoughts =====
we could optimize this by binary searching after sorting

~~Complexity Analysis
Time - O(nlogn + logn)
Space - O(1)

we just have to answer... what becomes true at 3 (for each example)?
[0,1,3,5,6] val at 2 >= N - 2
[1,1,3]

failed on edge case
[0]... should be 0, not 1...
[0]
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        citations.sort()
        l, r = 0, N - 1
        while l < r:
            mid = l + ((r - l) // 2)
            if citations[mid] >= N - mid:
                r = mid
            else:
                l = mid + 1
        return N - l if citations[l] else 0
