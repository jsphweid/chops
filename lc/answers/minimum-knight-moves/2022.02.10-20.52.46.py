"""
===== Initial Thoughts =====
brute force would be to do bfs but it'd quickly get out of control
but with a cache, you could prune a lot of paths
maybe even using distance between two points to see if it's improving or not would be better
then again we could use a minimum heap maybe?

=== Implemented Approach ===
Let's try BFS with cache and see what happens

Cool, it TLE'ed as expected.

One thing we need to add... there's little point to going in the wrong direction. ESPECIALLY if it's not really close.

first one that passes... but it is VERY slow
import math
def get_distance(x, y, xx, yy):
    _x, _y = (x - xx) ** 2, (y - yy) ** 2
    return math.sqrt(_x + _y)

from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        res, seen, queue = -1, set(), deque([(0,0)])
        while queue:
            res += 1
            for _ in range(len(queue)):
                xx, yy = queue.popleft()
                if (xx, yy) in seen:
                    continue
                seen.add((xx, yy))
                if x == xx and y == yy:
                    return res
                curr = get_distance(x, y, xx, yy)
                for pair in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
                    nxt_x, nxt_y = pair[0] + xx, pair[1] + yy
                    nxt = get_distance(x, y, nxt_x, nxt_y)
                    if nxt < curr or nxt < 5:
                        queue.append((nxt_x, nxt_y))

What if we could cut down width by two though? Currently up to 4 nodes will be going in the direction
but we really only need the two best ones I think.

What's the complexity here? The height of the tree is basically the linear distance between source and destination.
The width worst case can get pretty bad. Our comparison is not great because it only improves over the the last node.
That allows paths to get off and circle around the destination instead of going directly to it.

It'd be better if we had some global 'best' and culled any path that got to far off of it.

~~Complexity Analysis
Time - 
Space - 
"""

import math
from collections import deque

def get_distance(x, y, xx, yy):
    _x, _y = (x - xx) ** 2, (y - yy) ** 2
    return math.sqrt(_x + _y)

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        res, seen, queue, closest = -1, set(), deque([(0,0)]), math.inf
        while queue:
            res += 1
            for _ in range(len(queue)):
                xx, yy = queue.popleft()
                if x == xx and y == yy:
                    return res
                if (xx, yy) in seen:
                    continue
                seen.add((xx, yy))
                curr = get_distance(x, y, xx, yy)
                closest = min(closest, curr)
                if curr - closest > 2:
                    continue

                for pair in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
                    nxt_x, nxt_y = pair[0] + xx, pair[1] + yy
                    nxt = get_distance(x, y, nxt_x, nxt_y)
                    if nxt < curr or nxt < 5:
                        queue.append((nxt_x, nxt_y))
