"""
===== Initial Thoughts =====
we could use bisect left...

~~Complexity Analysis
Time - O(log n)
Space - O(1)
"""

import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)