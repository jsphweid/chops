class MyQueue:
    def __init__(self):
        self._queue = []

    def add(self, x: int) -> None:
        self._queue.append(x)

    def remove(self) -> int:
        return self._queue.pop(0)

    def empty(self) -> bool:
        return len(self._queue) == 0

    def top(self) -> int:
        return self._queue[0]


class MyStack:

    def __init__(self):
        self._top_queue = MyQueue()
        self._bottom_queue = MyQueue()

    def push(self, x: int) -> None:
        if not self._top_queue.empty():
            self._bottom_queue.add(self._top_queue.remove())
        self._top_queue.add(x)

    def pop(self) -> int:
        item = self._top_queue.remove()
        removals = 0
        while not self._bottom_queue.empty():
            self._top_queue.add(self._bottom_queue.remove())
            removals += 1
        for _ in range(removals - 1):
            self._bottom_queue.add(self._top_queue.remove())
        return item

    def top(self) -> int:
        return self._top_queue.top()

    def empty(self) -> bool:
        return self._top_queue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()