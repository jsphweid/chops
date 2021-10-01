"""
===== Initial Thoughts =====
keep var for size, and for window (queue)
when new item is added, increase length if size is not large enough
if it's too large, then pop item out of the queue
"""

class MovingAverage:

    def __init__(self, size: int):
        self._size = size
        self._queue = []
        self._current_sum = 0

    def next(self, val: int) -> float:
        if len(self._queue) == self._size:
            # it's already at capacity
            old = self._queue.pop(0)
            self._current_sum -= old
        self._queue.append(val)
        self._current_sum += val
        return self._current_sum / len(self._queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)