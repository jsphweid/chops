"""
[5,10,-5]
1,3 -> 1, 2
1 - left=5 right=10
2 - left=10 right=-5
[5,10,-5]
[5,10]

[2,3,8,-8,5,6]
i=3 
asteroids = [2,3] + [5,6]

[2,3,8,-8,5,6,-7]
[2,3,5,6,-7]

[10,3,8,-8,7,6,-7]
[10,3]

[8,-8]
[]

[10,2,-5]
[10]

keeper=7
[2,3,8,-8,7,5,-6]
[2,3,7]

[2,3,7]

keeper=-5
[5,10,-5]
[5,10]

k=-2
[1,-2,-2,-2]
[-2,-2,-2]
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = [asteroids[0]]
        for i in range(1, len(asteroids)):
            keeper = asteroids[i]
            append = True
            while res and keeper < 0 and res[-1] > 0:
                if res[-1] == abs(keeper):
                    res.pop()
                    append = False
                    break
                else:
                    keeper = res[-1] if res[-1] > abs(keeper) else keeper
                    res.pop()
            if append:
                res.append(keeper)
        return res

