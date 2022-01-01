"""
i=2 j=1

0, 0
recurse(0, 0)
    recurse(1, 0)
        recurse(2, 0)
            recurse(2, 1)
        recurse(1, 1)
            recurse(2, 1)
    recurse(0, 1)
        recurse(1, 1)
            recurse(2, 1)

recurse(3, 2)
    recurse(2, 2)
        recurse(1, 2)
    recurse(3, 1)

works but times out
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        else:
            down = self.uniquePaths(m - 1, n) if m > 1 else 0
            right = self.uniquePaths(m, n - 1) if n > 1 else 0
            return down + right


3x2 (3)
3 spaces, 1 R, 2 D's
DDR
DRD
RDD

3x3 (6)
4 spaces, 2 R's, 2 D's
RRDD
RDDR
RDRD
DRRD
DRDR
DDRR

2___

4x3 (10)
5 spaces, 2 R's, 3 D's
RRDDD
RDRDD
RDDRD
RDDDR
DRRDD
DRDRD
DRDDR
DDRRD
DDRDR
DDDRR

3x7 (28)
8 spaces, 6 R's, 2 D's

I LOOKED IT UP
but it's a simple formula I guess I just have to memorize?
"""
from math import factorial as fac
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        m, n = m - 1, n - 1
        return int(fac(m + n) / (fac(m) * fac(n)))
