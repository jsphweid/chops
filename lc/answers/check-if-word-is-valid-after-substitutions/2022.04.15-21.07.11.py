"""
===== Initial Thoughts =====
"aabcbc"
"aabcbc"

"ababcc"
""

cba

abccba


=== Implemented Approach ===
just use a stack

~~Complexity Analysis
Time - O(n)
Space - O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "c":
                if len(stack) < 2:
                    return False
                if stack[-1] == "b" and stack[-2] == "a":
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0

