"""
===== Initial Thoughts =====
thinking about this... when you combine a number an its compliment, it equals 11111...
etc.

so really we just need to get the nearest 111111 and subtract the given number from it
it can be found by using log(n, 2) to find the number of zeros, then get the power, etc.

5 => 101
nearest is 111, which is 7, 2 ** (int(log(5, 2)) + 1) - 1 or something like that
"""
from math import log
class Solution:
    def findComplement(self, num: int) -> int:
        return (2 ** (int(log(num, 2)) + 1) - 1) - num