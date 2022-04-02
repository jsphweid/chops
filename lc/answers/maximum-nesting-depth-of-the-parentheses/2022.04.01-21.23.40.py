"""
===== Initial Thoughts =====
pretty sure we can just ignore anything not ( or )
and keep a stack whose length is the max depth at any given time

~~Complexity Analysis
Time - O(n)
Space - O(n) (because in string like "(((())))" it can be half of N, which is N)

Actually we don't need to keep the stack... we can just keep a number...

Time - O(n)
Space - O(1)
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        curr = res = 0
        for char in s:
            if char == "(":
                curr += 1
                res = max(res, curr)
            elif char == ")":
                curr -= 1
        return res
