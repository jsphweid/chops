"""
===== Initial Thoughts =====

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [
            (1, "I"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (40, "XL"),
            (50, "L"),
            (90, "XC"),
            (100, "C"),
            (400, "CD"),
            (500, "D"),
            (900, "CM"),
            (1000, "M"),
        ]
        res = ""
        while num:
            if num >= nums[-1][0]:
                res += nums[-1][1]
                num -= nums[-1][0]
            else:
                nums.pop()
        return res