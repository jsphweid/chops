class MyStack:
    def __init__(self):
        self._stack = []
    def push(self, val):
        self._stack.append(val)
    def size(self):
        return len(self._stack)
    def is_empty(self):
        return self.size() == 0
    def peek(self):
        return None if self.is_empty() else self._stack[-1]
    def pop(self):
        # NOTE: will blow up if no value exists...
        return self._stack.pop()


"""
queue: [1, 2, 5, 7, 4]

top stack: []
bottom stack: []

pop 4

"""

class MyQueue:

    def __init__(self):
        self._top_stack = MyStack()
        self._bottom_stack = MyStack()


    def push(self, x: int) -> None:
        if self._top_stack.is_empty():
            self._top_stack.push(x)
        else:
            self._bottom_stack.push(x)


    def pop(self) -> int:
        ret = self._top_stack.pop()
        bottom_size = self._bottom_stack.size()
        if bottom_size:
            for _ in range(bottom_size - 1):
                self._top_stack.push(self._bottom_stack.pop())
            next_item = self._bottom_stack.pop()
            for _ in range(bottom_size - 1):
                self._bottom_stack.push(self._top_stack.pop())
            self._top_stack.push(next_item)
        return ret


    def peek(self) -> int:
        return self._top_stack.peek()
        

    def empty(self) -> bool:
        return self._top_stack.is_empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()