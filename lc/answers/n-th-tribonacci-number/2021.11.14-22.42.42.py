"""
n = 4

a=0 b=1 c=1
res=2 a=1 b=1 c=2
res=4 a=1 b=2 c=4

"""

class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        easy = {0: a, 1: b, 2: c}
        if n <= 2: return easy[n]
        for _ in range(n - 2):
            res = a + b + c
            a = b
            b = c
            c = res
        return res