"""
===== Initial Thoughts =====
DIDIIDDIDIID
[1,0,2,-1,3,4,-2,-3]

=== Implemented Approach ===
pretty sure we start at 1, then keep pointers for max and min and spread
stuff out gradually. At the very end, we use the min to lift everything up
by some constant so the smallest number is 1...

~~Complexity Analysis
Time - O(n)
Space - O(n)

failed on
"DDIIDI"
[1,0,-1,2,3,-2,4]

I got this
[4,3,2,5,6,1,7]

but we expected
[3,2,1,4,6,5,7]

This means I've fundamentally not solved the problem.

"DDIIDI"
[3,2,1,4,6,5,7]
we could use a stack but it'd get pretty expensive... I think I'll need to sleep on this

"DDIIDIIIDD"
[3,2,1,4,6,5,7,8,11,10,9]

[3,2,1,4,6,5,7,8,9]
brute force would be to use a stack, but it's very expensive in cases like DDDDDD
[1]
[2,1]
[3,2,1] n^2

3 2 1     6 5     11 10 9

3 2 1     5 4       8 7 6
3 2 1  4  6 5     

[2, 2, 1, 3, 2]
[3,2,1]
[3,2,1]
inc=0 [3,2,1]
inc=3 [4]
inc=4 [6,5]
inc=6 [7,8]
inc=8 []

1

"DDIIDIIIDD"
[2, 1, 2, 1, 1, 3]

2 2 1 1
"DDIIDI"
[3,2,1,4,6,5,7]
[3,2,1] + [4] + [6,5] + [7]
1 2 3 4 5 6 7

"DDDIIDI"

"IIDDID"
1 2 5 4 3 7 6
1 2 5 4 3 7 6

1 2 5 4 3 7 6


"IIDDID"
1 2 5 4 3 7 6

2 2 1 1 -> 1 3 0 2

"DDIIDI"
2 2 1 1 -> 3 1 2 0
3 2 1 4 6 5 7

3 2 1 4 6 5
7

DDIIDID
[3,2,1,4,6,5,8,7]
3 2 1 4 6 5 8 7
3 1 2 0 2

IIDD
1 2 5 4 3
res=[1,2]
stack=[3,4,5]

DDIIDID
3 2 1 4 6 5 8 7 chr

3 2 1 4 5 6 7 8

Read the solutions because I ain't got any more time to waste.
"""

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        res, stack = [], [1]
        num = 1
        for char in s:
            num += 1
            if char == "I":
                while stack:
                    res.append(stack.pop())
            stack.append(num)
        while stack:
            res.append(stack.pop())
        return res






