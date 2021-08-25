"""
n=1, output 1 (1)
n=2, output 2 (1+1, 2 step)
n=3, output 3 (1+1+1, 1+2, 2+1)
n=4, output 5 (1+1+1+1, 1+1+2, 2+1+1, 1+2+1, 2+2)
n=5, output 8 (1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+2+1, 2+1+2)
n=6, output 13 (1+1+1+1+1+1, 1+1+1+1+2, 1+1+1+2+1, 1+1+2+1+1, 1+2+1+1+1, 2+1+1+1+1, 1+1+2+2, 1+2+1+2, 2+1+1+2, 2+1+2+1, 2+2+1+1, 1+2+2+1, 2+2+2)

it's fibonacci sequence. I've never implemented this directly so we'll see how this goes.

if 1, return 1
if 2, return 2

a = 1
b = 2

start at some point, increment until we reach the number (so like while x <= n)
each iteration, we can get the new output, and update the nums so next iteration has something
good to use

The only question is what are the starting values. I think what I have above might work.
I just need to start x at 3. This will compute a+b=3. update a=b. b=x (3). go to next.
x=4, a+b==2+3... do the same updates etc. should work out

Actually, we should start at 4 to save a single iteration
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        a = 2
        b = 3
        x = 4
        result = None
        while x <= n:
            result = a + b
            a = b
            b = result
            x = x + 1
        return result