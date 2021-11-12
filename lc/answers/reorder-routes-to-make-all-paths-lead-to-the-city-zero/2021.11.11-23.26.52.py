"""
===== Initial Thoughts =====
[[0,1],[1,3],[2,3],[4,0],[5,4]] [1,0],[3,1],
a = [[0,1],[1,3],[2,3],[4,0],[4,5]]
tos = [4,5] # 1,4,0,3,2 (nodes we can attach to) switched=2
# if it doesn't contain any nodes we've seen, skip
# if it contains the node we've seen in the correct placement, delete it, and add tail
# if it contains node we've seen in incorrect place, reverse it, increment count, delete it, add tail
do this until no nodes are left

tracing

[[0,1],[1,3],[2,3],[4,0],[4,5]]
seen={0,1,3,2,4,5} count=2 q=[[4,5]]
"""
from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        seen = {0}
        q = deque(connections)
        count = 0
        while len(q):
            c_from, c_to = q.popleft()
            if c_from not in seen and c_to not in seen:
                q.append([c_from, c_to])
            elif c_to in seen:
                seen.add(c_from)
            else:
                count += 1
                seen.add(c_to)
        return count