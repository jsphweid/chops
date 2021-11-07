"""
===== Initial Thoughts =====
start with (

n=3

(, 1, 0
((, 2, 0
(), 1, 1
(((, 3, 0
------

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        strs = []
        def recurse(s, l, r):
            if l == n and r == n:
                strs.append(s)
            if l < n:
                recurse(s + "(", l + 1, r)
            if r < l:
                recurse(s + ")", l, r + 1)
        recurse("(", 1, 0)
        return strs