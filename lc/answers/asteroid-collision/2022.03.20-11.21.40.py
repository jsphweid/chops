"""
===== Initial Thoughts =====
I need a bigger example
[5,10,2,-3,4,-9,22,-1]
should be pretty easy to do with a stack

=== Implemented Approach ===
use a stack to add numbers to. constantly check the top to see if an
interaction occurs, if it does, then produce the result. But then check
to see if another interaction occurs.

~~Complexity Analysis
Time - O(n)
Space - O(n)

[5,10,2,-3,4,-9,22,-1]
[5,10,22]
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for asteroid in asteroids:
            add_asteroid = True
            if res:
                while res and res[-1] > 0 and asteroid < 0:
                    last = res[-1]
                    if -last == asteroid:
                        res.pop()
                        add_asteroid = False
                        break
                    elif -last < asteroid:
                        add_asteroid = False
                        break
                    else:
                        res.pop()
            if add_asteroid:
                res.append(asteroid)
        return res






