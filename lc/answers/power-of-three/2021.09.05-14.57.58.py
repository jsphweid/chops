import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        # if the exponent is an int, it's a power of 3
        return 3 ** round(math.log(n, 3)) == n


"""
failed a couple of times but learned some stuff

this would be a lot easier if math.log(n, 3) returned an integer
instead of 4.99999 or whatever. But it's not too hard to keep that
since we can just round to nearest enter and cube which should
give us n if the rounding was just correcting a floating point
error.
"""