"""
~~Complexity Analysis
n is the length if shift
m is the length of the string
Time - O(n + m)
Space - O(m)
"""
from collections import deque
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final_shift = 0
        for direction, quantity in shift:
            if direction:
                final_shift += quantity
            else:
                final_shift -= quantity
        final_shift = final_shift % len(s)
        queue = deque(s)
        for _ in range(abs(final_shift)):
            if final_shift > 0:
                queue.appendleft(queue.pop())
            else:
                queue.append(queue.popleft())
        return "".join(queue)