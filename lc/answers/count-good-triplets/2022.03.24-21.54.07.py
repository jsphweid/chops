"""
=== Brute Force Approach ===
just try all possibilities

~~Complexity Analysis
Time - O(n^3)
Space - O(1)

=== Implemented Approach ===
[3,0,1,1,9,7]
[0,1,1,3,7,9] a = 7, b = 2, c = 3

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def countGoodTriplets(self, L: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for i in range(len(L) - 2):
            for j in range(i + 1, len(L) - 1):
                if abs(L[i]-L[j]) <= a:
                    for k in range(j + 1, len(L)):
                        if abs(L[i]-L[k])<=c and abs(L[j]-L[k])<=b:
                            res += 1
        return res