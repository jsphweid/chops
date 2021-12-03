"""
===== Initial Thoughts =====
we have to figure out the best way to get from point A to point B
using diags are the best choice if we have to move in two directions
otherwise the best is always a single 1 move

1,1 -> 2,2 => 1
1,1 -> 3,3 => 2
1,1 -> 3,4 => 3 (the 2 above and then 1 more)

How do we derive how many diags we can take?

what about 3,4 -> -1,0? It's kind of limited by the least absolute diff
3 to -1
4 to 0... both are 4, which is the result.

But on the ones above, 1,1 -> 3,4
1-3 and 1-4... min is 2 diags (abs(1-3))... subtracting 2 from the other 
abs difference is abs(1-4), 3-2 => 1.. so it's 2+1

actually, couldn't you just take the highest... abs(1-4) => 3
if you have 2 numbers

makes sense... we just have to code it

~~Complexity Analysis
Time - O(n)
Space - O(1)
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            (x0, y0), (x1, y1) = points[i - 1], points[i]
            time += max(abs(x0 - x1), abs(y0 - y1))
        return time