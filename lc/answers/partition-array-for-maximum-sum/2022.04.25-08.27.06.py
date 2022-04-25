"""
===== Initial Thoughts =====
arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4

=== Brute Force Approach ===
just try every sublist
input is small enough this just might be the solution

~~Complexity Analysis
Time - O(k^n) ??
Space - O(n)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

1 3 2, k=2 (result should be 8)
N=3
recurse(0)
    # largest=1 res=-1 total=1
    0
        1 + recurse(1)
            # largest=-1 res=-1 total=1
    1
        3

Damn, so I got stuck on this for a while because i used 'i' instead of 'j' in a place or two
that made no sense.
"""

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)

        @cache
        def recurse(i):
            if i == N: return 0
            largest = res = -float("inf")
            for j in range(i, min(N, i + k)):
                largest = max(largest, arr[j])
                total = largest * (j - i + 1)
                res = max(res, total + recurse(j + 1))
            return res
        return recurse(0)
