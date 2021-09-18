"""
what happens if you popMax and max isn't the top most element, does it pop everything else in its way?
It isn't clear from the instructions. I'm going to assume actually it's that it just pops the max even
if it's not the top...
"""

class MaxStack:

    def __init__(self):
        self._stack = []
        
    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1] if len(self._stack) else None

    def peekMax(self) -> int:
        return max(self._stack)

    def popMax(self) -> int:
        max_num = max(self._stack)
        i = self._stack[::-1].index(max_num)
        return self._stack.pop((i + 1) * -1)

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()