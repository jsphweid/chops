"""
===== Initial Thoughts =====


=== Brute Force Approach ===
linear scan

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== Implemented Approach ===
use binary search

~~Complexity Analysis
Time - O(nlogn)
Space - O(1)

NOTE: analysis avoids k construction and comparison
we have to do those n/k times for the n^2
only log(n/k) times for the logn
"""

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        l, r = 0, (len(sequence) // len(word)) + 1
        while l < r:
            mid = (l + r) // 2
            if word * mid in sequence:
                l = mid + 1
            else:
                r = mid
        return l - 1
