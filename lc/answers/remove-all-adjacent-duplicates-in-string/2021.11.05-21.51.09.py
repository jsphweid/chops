"""
===== Initial Thoughts =====


=== Brute Force Approach ===
loop over the list and each time search for two duplicate conjoined letters and removing them
we could use regex...
([a-z])\1 (it's probably more efficient for finding two adjacent characters)

~~Complexity Analysis
Time - O(n^2)
Space - O(1) - use argument str

=== Implemented Approach ===
azxxzy
"".join(["a", "y"])

-----
aaaaa
"".join(["a"]) => "a"

""


add a new item to the stack
but if the stack contains at least one item, we should check if the current item is the same as the top of the stack
if it is, then we pop the item off the stack and continue the for loop... and repeat that process indefinitely until
we can proceed ???

~~Complexity Analysis
Time - 
Space - 
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) and stack[-1] == char:
                stack.pop()  # gets rid of one duplicate
            else:
                stack.append(char)
        return "".join(stack)


