"""
4**2 = 16
4**3 = 64
4**4 = 256
4**5 = 1024

I think you can solve this in a similar way to my "power of three"
solution, where you use logarithms

But you might be able to use simple squares here and be fine. My initial
thought on this would be to do the square root twice, but I don't think it
can work like that actually. (1024 ** 0.5) ** 0.5 doesn't work. That'd make
sense for maybe 4^4 or 4^8 etc. but probably not your normal of 4 because
it's just an incorrect understanding.

Also 64 ** (1/4) doesn't seem to work. I don't intuitively grasp
why, but it may not matter for now. I can always investigate that later

At this point I'm just going to go with my other solution as it is not
only adequate but a well engineered one I believe
"""

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n < 1 else 4 ** round(math.log(n, 4)) == n