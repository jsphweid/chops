"""
===== Initial Thoughts =====
00
10
11
01

000 - 0
001 - 1
011 - 3
010 - 2
110 - 6
111 - 7
101 - 5
100 - 4

0000 - 0
0001 - 1
0011 - 3
0010 - 2
0110 - 6
0111 - 7
0101 - 5
0100 - 4
1100 - 12
1101 - 13
1111 - 15
1110 - 14
1010 - 10
1011 - 11
1001 - 9
1000 - 8

0 3 6 5 12 15 10 9


=== Brute Force Approach ===
would be to calculate each string manually

~~Complexity Analysis
Time - n * 2^n
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def grayCode(self, n: int) -> List[int]:
        lst = ['0', '1']
        for _ in range(n - 1):
            lst = ['0' + s for s in lst] + ['1' + s for s in lst[::-1]]
        return [int(s, 2) for s in lst]