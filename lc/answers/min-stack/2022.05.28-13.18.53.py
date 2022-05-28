"""
===== Initial Thoughts =====
easy to think of O(n) ways of getting the minimum
[-2,0,-3]
but how do you do it in constant time?
after the -3 is popped, we need to know the next minimum is -2
we probably need some other data structure
a sorted dict but that's not even O(1)
we could make it so that pop is non constant time but that's probably not ideal either.

what about a min heap + set?
when we pop an item off that's not minimum, we add it to a set?

did some non-optimal approach. Then read in the back "stack with pair"

How can pairs help us?

Well now I remember. We store the minimum value seen up to the point in the stack
with the value itself
"""

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        prev_min = self.stack[-1][1] if self.stack else float("inf")
        new_min = min(prev_min, val)
        self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()