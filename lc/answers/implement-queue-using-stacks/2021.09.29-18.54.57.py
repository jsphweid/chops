class MyQueue:

    def __init__(self):
        self._top_stack = []
        self._bottom_stack = []

    def push(self, x: int) -> None:
        self._top_stack.append(x)

    def pop(self) -> int:
        while len(self._top_stack):
            self._bottom_stack.append(self._top_stack.pop())
        ret = self._bottom_stack.pop()
        while len(self._bottom_stack):
            self._top_stack.append(self._bottom_stack.pop())
        return ret        

    def peek(self) -> int:
        while len(self._top_stack):
            self._bottom_stack.append(self._top_stack.pop())
        ret = self._bottom_stack[-1]
        while len(self._bottom_stack):
            self._top_stack.append(self._bottom_stack.pop())
        return ret

    def empty(self) -> bool:
        return not len(self._top_stack)