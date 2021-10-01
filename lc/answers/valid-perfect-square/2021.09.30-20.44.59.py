"""
===== Initial Thoughts =====
I initially really misunderstood this problem for this second submission.
I thought it was "power of 2" but it's instead "perfect square". So that's the reasons
for some failed submissions.

=== Brute Force Approach ===
do some BS with searching every number starting at 0 until  it reaches or bypasses the number.


~~Complexity Analysis
Time - O(sqrt(n))
Space - O(1)

=== Implemented Approach ===
let's do binary search!

~~Complexity Analysis
Time - O(logn)
Space - O(1)
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return True
        left, right = 0, num
        while left < right:
            mid = (left + right) // 2
            sq = mid ** 2
            if num == sq: return True
            if sq > num: right = mid
            else: left = mid + 1
        return False
