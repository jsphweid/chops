"""
MCMXCIV
last=1000 res=1994
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        stack = list(s)
        mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        last = res = 0
        while stack:
            curr = mapping[stack.pop()]
            if curr < last:
                res -= curr
            else:
                res += curr
            last = curr
        return res