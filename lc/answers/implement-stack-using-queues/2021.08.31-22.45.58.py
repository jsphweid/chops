class MyQueue:
    def __init__(self):
        self._data = []
    def push(self, val):
        self._data.append(val)
    def peek(self):
        return self._data[0] if len(self._data) else None
    def pop(self):
        # NOTE: unsafe... only pop if you know there is something there!
        return self._data.pop(0)
    def size(self):
        return len(self._data)
    def is_empty(self):
        return self.size() == 0

"""
push 5
push 4
pop 4
push 2
pop 2
pop 5

stack
[5]

queues
[]
[]
"""

class MyStack:

    def __init__(self):
        self.top_queue = MyQueue()
        self.bottom_queue = MyQueue()

    def push(self, x: int) -> None:
        if self.top_queue.peek():
            previous = self.top_queue.pop()
            self.bottom_queue.push(previous)
        self.top_queue.push(x)

    def pop(self) -> int:
        ret = self.top_queue.pop()
        bottom_size = self.bottom_queue.size()
        for _ in range(bottom_size):
            item = self.bottom_queue.pop()
            self.top_queue.push(item)
        for _ in range(bottom_size - 1):
            item = self.top_queue.pop()
            self.bottom_queue.push(item)
        return ret

    def top(self) -> int:
        return self.top_queue.peek()
        

    def empty(self) -> bool:
        return self.top_queue.is_empty() and self.bottom_queue.is_empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()