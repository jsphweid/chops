"""
after reading the answer, we can modify the original num in-place and return it (it's copied anyways
since it's primitive). The cool thing about this approach is that the num-counter eventually runs out
of numbers if you keep shifting... so it makes a convenient exit condition... You don't have to use
log to count the digits...
"""

class Solution:
    def findComplement(self, num: int) -> int:
        counter = num
        flipper = 1
        while counter:
            num ^= flipper
            flipper = flipper << 1
            counter = counter >> 1
        return num