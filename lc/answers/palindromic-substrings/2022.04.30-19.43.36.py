"""
=== Brute Force Approach ===
go through each letter and expand wider to check for palindrones

~~Complexity Analysis
Time - O(n^2)
Space - O(1)

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0

        def count(l, r):
            nonlocal res
            while l >= 0 and r < N and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        for i in range(N):
            count(i, i)
            if i > 0: count(i - 1, i)
        return res
