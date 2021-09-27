"""
===== Initial Thoughts =====
use a stack, I think it's the most obvious way

=== Implemented Approach ===
if it's an opening item, push it to the stack
if it's a closing item, pop whatever is on there and assert it's the compliment

edge cases? it's empty, but constraint says there is at least one item

Error... didn't initially consider an input like "["... stack has to be empty for it to be valid!

~~Complexity Analysis
Time - O(n)
Space - O(n) maybe O(n/2) if it is valid, but it could be closer to O(n) if it is invalid
"""

class Solution:
    def isValid(self, s: str) -> bool:
        matching = {"{": "}", "[": "]", "(": ")"}
        stack = []
        for char in s:
            if char in matching.keys():
                stack.append(char)
            else:
                if not (len(stack) and char == matching.get(stack.pop())):
                    return False
        return len(stack) == 0