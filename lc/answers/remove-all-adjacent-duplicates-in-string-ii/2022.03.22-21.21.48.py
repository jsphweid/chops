"""
===== Initial Thoughts =====
pbbcggttciiippooaais k = 2

deeedbbcccbdaa k = 3

I don't quite know how but I'm fairly certain it just works out if we
use a stack here...

deeedbbcccbdaa
stack=[(d,1),(e,1),(e,2),()]

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            num = stack[-1][1] + 1 if stack and stack[-1][0] == char else 1
            stack.append((char, num))

            if stack and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
        return "".join([char for char, _ in stack])
