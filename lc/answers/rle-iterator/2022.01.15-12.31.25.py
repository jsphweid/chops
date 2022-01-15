"""
[2,5]
1,2
2,5
n=1
"""

from collections import deque
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.q = deque(encoding)

    def next(self, n: int) -> int:
        while n:
            if not self.q:
                return -1
            quantity, val = self.q.popleft(), self.q.popleft()
            n -= quantity
            if n < 0:
                self.q.appendleft(val)
                self.q.appendleft(abs(n))
                return val
        return val


