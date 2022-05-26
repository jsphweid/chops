"""
use a stack
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ")]}":
                if stack:
                    comp = stack.pop()
                    if char == ")" and comp != "(": return False
                    if char == "]" and comp != "[": return False
                    if char == "}" and comp != "{": return False
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0