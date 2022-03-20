"""
===== Initial Thoughts =====
just trying to do this more compactly after seeing another solution in the discussions.

collision cases (note bigger means absolute value bigger)
left is bigger - right just disappears
both are same size - left and right disappear
right is bigger - left disappears and right stays!

failed on [8,-8]
res=[8]
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            while res and res[-1] > 0 and a < 0:
                collision = res[-1] + a
                if collision <= 0: res.pop()
                if collision >= 0: break
            else:
                res.append(a)
        return res