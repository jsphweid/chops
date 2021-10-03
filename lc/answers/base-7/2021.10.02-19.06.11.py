"""
===== Initial Thoughts =====
should be able to use standard base conversion here

100

3 = 0 (0 343's)
2 = 2 (2 49's)
1 = 0 (0 7's)
0 = 2 (2 1's)

"""
from math import log
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        is_negative = num < 0
        abs_num = abs(num)
        num_digits = int(log(abs_num, 7)) + 1
        output = ""
        i = num_digits
        while i >= 0:
            fits = abs_num // (7 ** i)
            if output or fits:
                output += str(fits)
                if fits: abs_num -= (fits * (7 ** i))
            i -= 1
        return f"-{output}" if is_negative else output