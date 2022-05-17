"""
we're trying to find the last that is less than or equal to x
x=4
[0,1,2,3,4]
[T,T,T,F,F] (looking for right-most T)

x=8
[0,1,2,3,4,5,6,7,8]
[T,T,T,F,F,F,F,F,F] (looking for right-most T)

so we want to just find the first F then subtract 1.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (l + r) // 2
            if mid * mid > x:
                r = mid
            else:
                l = mid + 1
        return l if l * l == x else l - 1