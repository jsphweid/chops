"""
===== Initial Thoughts =====
[[0,1],[1,3],[2,3],[4,0],[4,5]]
[1,0],[3,1],[2,3],[4,0],[5,4]

"""
from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        pointable = set([0])
        queue = deque(connections)
        while queue:
            from_, to_ = queue.popleft()
            if to_ in pointable:
                pointable.add(from_)
            elif from_ in pointable:
                res += 1
                pointable.add(to_)
            else:
                queue.append([from_, to_])
        return res
