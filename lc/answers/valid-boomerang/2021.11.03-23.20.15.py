"""
===== Initial Thoughts =====
the right way to think about this problem is that... two points for a line. All we
have to do is determine whether or not the third point is on that line...

I failed a bunch because evidently I don't understand how to determine whether a point is on a line or not...

for a point to be on some line... it:
    - has to have the same slope and....??

still failing on this...
[[0,1],[0,1],[2,1]] 

now failing on this
[[92,72],[12,40],[27,46]]

The problem is rounding / floating point...

        if (points[0] == points[1]) or (points[1] == points[2]) or (points[0] == points[2]):
            # if two points are the same... we always return false
            return False

        # slope is rise over run...
        rise = points[0][1] - points[1][1]
        run = points[0][0] - points[1][0]

        if not run:  # it's a vertical line
            # this means the third point has to be on the same x... y doesn't matter
            # but remember we care about the inverse... so we use !=
            return points[2][0] != points[0][0]

        m = rise / run
        print('m', m)

        # y = mx + b... b = y - mx
        b = points[0][1] - (m * points[0][0])
        print('b', b)

        # y = mx + b.... 0 = y - mx - b
        # 0 would mean that it's a point on the line... so == 0 would return True... 
        # but we want False... so we'll return != 0...
        return points[2][1] - (m * points[2][0]) - b != 0


ok, had to look up area of triangle formula unfortunately

"""

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x0, y0 = points[0]
        x1, y1 = points[1]
        x2, y2 = points[2]
        return (((x0-x1)*(y0-y2))-((x0-x2)*(y0-y1))) != 0
