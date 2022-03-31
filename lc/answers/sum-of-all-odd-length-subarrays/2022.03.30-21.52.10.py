"""
=== Brute Force Approach ===
just create a sum, iterate every 2, sum up subarrays

~~Complexity Analysis
Time - ?
Space - O(n)

we'll figure out a more optimized way to do this next time...
"""

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i, res = 1, 0
        while i <= len(arr):
            for j in range(len(arr) - i + 1):
                res += sum(arr[j:j+i])
            i += 2
        return res