"""
This should be quite a bit easier than the reverse process. I think we can simply
go right to left and add up the (char * 26^n) where n is index starting from right
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        mapping = {val: i for i, val in enumerate("_ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
        for i, char in enumerate(reversed(columnTitle)):
            num += mapping[char] * (26 ** i)
        return num
