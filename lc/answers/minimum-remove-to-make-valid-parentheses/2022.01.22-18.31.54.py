"""
===== Initial Thoughts =====
(()))

)()

15 minutes of thinking not much but this idea
just keep track of all in a stack with indices and items
that are still on there we'll just remove from the string
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, char in enumerate(s):
            if char == ")":
                if len(stack) and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((char, i))
            elif char == "(":
                stack.append((char, i))

        ignore, res = set([i for _, i in stack]), ""
        for i, char in enumerate(s):
            res += "" if i in ignore else char
        return res
