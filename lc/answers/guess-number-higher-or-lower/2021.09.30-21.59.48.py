"""
===== Initial Thoughts =====
b-b-b-binary search
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, (2 ** 31)
        while left < right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0: return mid
            if result == 1: left = mid + 1
            elif result == -1: right = mid
