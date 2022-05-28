"""
===== Initial Thoughts =====
class MyQueue:

    def __init__(self):
        self.top = []
        self.bottom = []

    def push(self, x: int) -> None:
        if self.top:
            self.bottom.append(x)
        else:
            self.top.append(x)

    def pop(self) -> int:
        res = self.top.pop()

        if self.bottom:
            for _ in range(len(self.bottom) - 1):
                self.top.append(self.bottom.pop())
            nxt = self.bottom.pop()
            for _ in range(len(self.top)):
                self.bottom.append(self.top.pop())
            self.top.append(nxt)
        return res

    def peek(self) -> int:
        return self.top[0]
        

    def empty(self) -> bool:
        return not self.top


But now trying Pochmann's solution
"""

class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()