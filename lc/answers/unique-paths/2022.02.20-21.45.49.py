"""
m = 3, n = 2
m-1 = downs
n-1 = rights
DDR
DRD
RDD
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = m - 1, n - 1
        return math.factorial(m+n) // (math.factorial(m) * math.factorial(n))
