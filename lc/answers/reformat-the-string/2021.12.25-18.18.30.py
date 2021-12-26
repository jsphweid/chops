"""

"""
class Solution:
    def reformat(self, s: str) -> str:
        alpha, digits = [], []
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                alpha.append(char)
        if not (-2 < (len(alpha) - len(digits)) < 2):
            return ""
        first, second = (alpha, digits) if len(alpha) > len(digits) else (digits, alpha)
        res = ""
        curr = first
        while curr:
            res += curr.pop()
            curr = first if curr == second else second
        return res
