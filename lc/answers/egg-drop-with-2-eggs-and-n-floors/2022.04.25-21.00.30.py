"""
===== Initial Thoughts =====
oh this problem

n=100, output should be 14

9, 22, 34, 45, 55, 64, 72, 79, 85, 90, 94, 97, 99, 100, largest interval is 13 + 1

do we just always add 1 from the top?

n=10?
0 4 7 9
4       0,1,2,3 => 5
4,7     5,6 => 4
4,7,9   8 => 4
4,7,9,t => 4

0 3 7 9


n=2

1, 2, largest interval is 1 + 1

n=100
i=0 100
i=1 99
i=2 97
i=3 94
i=4 90
i=5 85
i=6 79
i=7 72
i=8 64
i=9 55
i=a 45
i=b 34
i=c 22
i=d 9

n=10
i=0 10
i=1 9
i=2 7
i=3 4
i=4 0

failed on 6
n=6
i=0 6
i=1 5
i=2 3
i=3 0

apparently n=10 is really 4...
n=10 
10
9
7
4
7

ah you can start from 1

10
i=1 9
i=2 7
i=3 4
i=4 0
i=5 -5
"""

class Solution:
    def twoEggDrop(self, n: int) -> int:
        interval = 0
        while n > 0:
            interval += 1
            n -= interval
        return interval
