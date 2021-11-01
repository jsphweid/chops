"""
===== Initial Thoughts =====
maybe we could do this with a stack?
10011
then just push everything and left shift back offf
1
0
0
1
1


1010
[0101]

0
"""

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        res, stack = 0, []
        while n:
            stack.append(n & 1)
            n >>= 1
        while len(stack):
            digit = stack.pop()
            res <<= 1
            res |= (not digit)
        return res