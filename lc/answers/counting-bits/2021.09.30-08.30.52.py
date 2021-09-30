"""
===== Initial Thoughts =====
I can't remember exactly how I solved this. The nlogn solution is "very easy to come up with"?
That means iterate once per number, then count 1s in logn time. I forget how to count 1s. 

0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
6 --> 110
7 --> 111
8 --> 1000
9 --> 1001
10 -> 1010
11 -> 1011
12 -> 1100
13 -> 1101
14 -> 1110
15 -> 1111
16 -> 10000

=== Brute Force Approach ===
iterate over each number count 1s

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []
        for i in range(n + 1):
            count = 0
            while i:
                count += (i & 1)
                i = i >> 1
            ret.append(count)
        return ret