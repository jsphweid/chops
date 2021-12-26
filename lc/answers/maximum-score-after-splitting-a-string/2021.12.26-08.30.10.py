"""
011101 
l=0 r=4
char=0 l=1 r=4
char=1 l=1 r=3
char=1 l=1 r=2
char=1 l=1 r=1
char=0 l=2 r=1
char=1 l=

"""

class Solution:
    def maxScore(self, s: str) -> int:
        l, r, res = 0, s.count("1"), 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                l += 1
            else:
                r -= 1
            res = max(res, l + r)
        return res