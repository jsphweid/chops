"""
===== Initial Thoughts =====


=== Brute Force Approach ===
keep subtracting the divisor until dividend < divisor. Use abs value

        num_neg = sum([dividend < 0, divisor < 0])
        top = abs(dividend)
        bottom = abs(divisor)
        count = 0
        while top >= bottom:
            top -= bottom
            count += 1
        return (count * -1) if num_neg & 1 else count

~~Complexity Analysis
Time - 
Space - 

=== Implemented Approach ===


~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        num_neg = sum([dividend < 0, divisor < 0])
        top = abs(dividend)
        bottom = abs(divisor)
        count = 0
        while top >= bottom:
            n = bottom
            ls = 0
            while n <= top:
                n = n << 1
                ls += 1
            top -= n >> 1
            count += 2 ** (ls - 1)
        final = (count * -1) if num_neg & 1 else count
        return min(final, 2147483647)

