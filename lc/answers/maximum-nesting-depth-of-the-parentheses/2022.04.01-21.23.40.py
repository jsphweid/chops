"""
===== Initial Thoughts =====
pretty sure we can just ignore anything not ( or )
and keep a stack whose length is the max depth at any given time

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        stack, res = [], 0
        for char in s:
            if char == "(":
                stack.append("(")
                res = max(res, len(stack))
            elif char == ")":
                stack.pop()
        return res