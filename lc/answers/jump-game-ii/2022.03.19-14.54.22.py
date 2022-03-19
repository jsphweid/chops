"""
from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        level = -1
        end = len(nums) - 1
        queue = deque([0])
        seen = set()
        while queue:
            level += 1
            for _ in range(len(queue)):
                i = queue.popleft()
                if i == end:
                    return level
                if i in seen or i > end:
                    continue
                seen.add(i)
                jump = nums[i]
                if jump:
                    for j in range(i + 1, i + jump + 1):
                        if j not in seen:
                            queue.append(j)
does very poorly. the problem is we don't really want to explore so many paths
even though bfs saves a lot of paths, it's not enough because the width of the tree
is so large -- bfs saves from deep trees

how about dijkstra's?

don't we want the i that's the farthest along but with the fewest moves?
I'm just afraid that we'll get to the end with something that is not ideal.

[2,3,1,1,4]

prefer higher, lower
i2 1
i1 1

that doesn't make much sense. If we order the heap via number moves, we essentially
making dfs. If we order by index, then we won't get the optimal answer (because we'll
always choose the farthest along as the first priority)

dijkstras isn't a good fit here I don't think

I think I remember the solution now. It's something like, look two 
jumps ahead to find the next most optimal jump.

2 3 1 1 4
  4 3
(4,1)
(3,2)

i=1 (1 to 4, so 1,2,3)

"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        i, jumps, end = 0, 0, len(nums) - 1
        while i != end:
            nxt = (0, 0)
            for j in range(1, nums[i] + 1):
                idx = i + j
                if idx == end:
                    return jumps + 1
                nxt = max(nxt, (nums[idx] + j, idx))
            i = nxt[1]
            jumps += 1
        return jumps


