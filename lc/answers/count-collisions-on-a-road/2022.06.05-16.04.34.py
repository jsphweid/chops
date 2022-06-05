"""
===== Initial Thoughts =====
RLRSLL

seems pretty straight forward with a stack

~~Complexity Analysis
Time - O(n)
Space - O(n)

RLRSLL
acc=1
total=5

FAILED On "LLSRSSRSSLLSLLLRSLSRL"
swiched the order of the if statements...

then failed on 

"SRRLRLRSRLRSSRRLSLRLLRSLSLLSSRRLSRSLSLRRS"
RRLRLRRLRRRLLRLLRLLLRRLRLLRR

it's really simpler than what I'm thinking...
We could just remove any L on the left up to first S/R
Then remove any R on the right up to the first S/L
Then count R/L

instead of 
class Solution:
    def countCollisions(self, directions: str) -> int:
        total = acc = 0
        stack = list(directions)
        while stack:
            curr = stack.pop()
            if curr == "L":
                acc += 1
            if curr == "R" or curr == "S":
                total += acc
                acc = 0
            if curr == "R":
                total += bool(total)
        return total

But why won't this work???

SRRLRLRSRLRSSRRLSLRLLRSLSLLSSRRLSRSLSLRRS
because it's not counting the two R's on the right. bool(total) isn't good enough.

class Solution:
    def countCollisions(self, directions: str) -> int:
        total = acc = 0
        stack = list(directions)
        right_blocked = False
        while stack:
            curr = stack.pop()
            if curr == "L" or curr == "S":
                right_blocked = True
            if curr == "L":
                acc += 1
            if curr == "R" or curr == "S":
                total += acc
                acc = 0
            if curr == "R":
                total += right_blocked
        return total

"""

class Solution:
    def countCollisions(self, directions: str) -> int:
        total = acc = 0
        stack = list(directions)
        right_blocked = False
        while stack:
            curr = stack.pop()
            if curr == "L" or curr == "S":
                right_blocked = True
            if curr == "L":
                acc += 1
            if curr == "R" or curr == "S":
                total += acc
                acc = 0
            if curr == "R":
                total += right_blocked
        return total
