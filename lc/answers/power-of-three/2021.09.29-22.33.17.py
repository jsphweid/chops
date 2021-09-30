"""
tracing

27
27 % 3 => 0
9
9 % 3 => 0
3 > 3 false!
n == 3
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        while n > 3:
            if n % 3 != 0: return False
            n //= 3
        return n == 3