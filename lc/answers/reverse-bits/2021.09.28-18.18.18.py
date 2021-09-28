"""
===== Initial Thoughts =====
I forgot how I solved this last time... maybe using strings?

=== Brute Force Approach ===
take away each bit and push it on a new number somehow

~~Complexity Analysis
Time - O(n) where n is the number of bits
Space - O(n)

=== Implemented Approach ===
the brute force
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            right_bit = (n >> i) & 1
            output = output << 1
            output = output | right_bit
        return output            