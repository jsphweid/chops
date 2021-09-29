"""
===== Initial Thoughts =====
lets use a loop

=== Implemented Approach ===
until n == 2, see if n divides evenly into 2. If it doesn't return False. If it does, change
n to be n//2. return true if it gets to the end

~~Complexity Analysis
Time - max is 32 loops for 32 bit int
Space - O(1)
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1: return False
        if n == 1: return True
        while n != 2:
            if n % 2 != 0: return False
            n //= 2
        return True