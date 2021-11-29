"""
===== Initial Thoughts =====
since we need nothing more than true or false, we can resort to comparing the slope
of the first two points. If it's a straight line, all points must be in alignment with
those two points.

I suspect we will deal with rounding errors, though.

~~Complexity Analysis
Time - O(n)
Space - O(1)

y = mx + b
y - mx


FAILED on... didn't consider division by 0
[[0,0],[0,1],[0,-1]]
"""
from math import inf
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]

        if x1 - x0 == 0:
            return all([c[0] == x1 for c in coordinates])

        m = (y1 - y0) / (x1 - x0)
        b = y0 - (m * x0)

        for x, y in coordinates:
            if y != (m * x + b):
                return False
        return True