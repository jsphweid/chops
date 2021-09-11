"""
Looking at the solution but not with too many details read... "To move along the number and flip bit by bit."
is a valid solution... Let's try that.
"""
import math

class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        num_binary_digits = math.floor(math.log(num, 2)) + 1
        for i in range(num_binary_digits):
            isolated = ((num >> i) & 1)
            flipped = isolated ^ 1
            readjusted = flipped << i
            result |= readjusted
        return result