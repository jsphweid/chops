"""
=== Brute Force Approach ===
simulation

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 

2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32

if it's a power of 2... then it should go down predictably
32 -> 6
33 -> 7
34 -> 7
35 -> 8
36 -> 7
37 -> 8
38 -> 8
39 -> 9
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num:
            res += 1
            if num & 1:
                num -= 1
            else:
                num //= 2
        return res