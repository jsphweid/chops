"""
===== Initial Thoughts =====
I think we can just do it 4 times (because max net diff for rotate is 90 * 4 360)
and if we encounter a 0,0 anywhere after each cycle it works. Gotta leave in 7 minutes.
Time to speed code.

failed 86/116 passed
failed on "RLLGGLRGLGLLLGRLRLRLRRRRLRLGRLLLGGL"
actually it failed because I accidentally had the "r" lowercase
it succeeded after that

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        shift = 0
        pos = (0, 0)
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        for inst in [instructions] * 4:
            for char in inst:
                x, y = pos
                if char == "G":
                    x_change, y_change = direction[shift % 4]
                    pos = (x + x_change, y + y_change)
                elif char == "L":
                    shift -= 1
                elif char == "R":
                    shift += 1
            if pos == (0, 0):
                return True
        return False

~~Complexity Analysis
Time - O(n)
Space - O(n)

=== Optimized Approach ===
We can do this in less memory O(1) and less time (although still O(n))

After the first time. We really just need to record the shift.


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        shift, pos, directions = 0, (0, 0), [(0,1),(1,0),(0,-1),(-1,0)]
        for char in instructions:
            x, y = pos
            if char == "G":
                x_change, y_change = directions[shift % 4]
                pos = (x + x_change, y + y_change)
            elif char == "L":
                shift -= 1
            elif char == "R":
                shift += 1

        if pos == (0, 0):
            return True

        diff = pos

        # I don't know much about this but we have a diff and rotation
        # and the diff. The rotation will affect the diff each iteration
        for _ in range(3):
            i = shift % 4
            if i == 0: # up - keep same
                pass
            elif i == 1: # left - swap and negate left num
                diff = (diff[1] * -1, diff[0])
            elif i == 2: # down - negate both
                diff = (diff[0] * -1, diff[1] * -1)
            else: # right - swap and negate right num
                diff = (diff[1], diff[0] * -1)
            pos = (pos[0] + diff[0], pos[1] + diff[1])
            if pos == (0, 0):
                return True
        return False


~~Complexity Analysis
Time - O(n)
Space - O(1)

So I know my solution works, but the thing I missed was that as long as we don't end with it
pointing up at a non-(0,0), it will eventually make it back. If it ends pointing down. Then
it'll make it back in 2 I think. If it ends pointing left or right, then it'll make it back
in 1 or 3.

An explanation I like is -- it's like a square -- you keep turning 90 and you're eventually
going to wind up at the place you started.
"""

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        shift, pos, directions = 0, (0, 0), [(0,1),(1,0),(0,-1),(-1,0)]
        for char in instructions:
            x, y = pos
            if char == "G":
                x_change, y_change = directions[shift % 4]
                pos = (x + x_change, y + y_change)
            elif char == "L":
                shift -= 1
            elif char == "R":
                shift += 1

        return (pos == (0, 0)) or (shift % 4 != 0)









