"""
It's just binary search
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min_num = 1
        max_num = 2 ** 31

        while True:
            midpoint = (min_num + max_num) // 2
            wrong = guess(midpoint)
            if not wrong:
                return midpoint
            elif wrong > 0:
                min_num = midpoint
            else:
                max_num = midpoint