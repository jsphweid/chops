"""
read the next answer but wanted to implement it on my own... creating a bitmask without iteration...
if the number is 3 bits long then we can ^ with 111 and it'll flip the bits appropriately.
But how do we get 111 without iteration?

We could just know it's the number 7... or 2**3 - 1. Honestly that's probably the simplest. But you
could also get 1000 (since that's easy with 1 << 4) then subtract 1 from it... I think (1 << 4) - 1
takes few instructions if I had to guess though (not 100% on that). But since that's what the answer
proposed, I'm going to go with my solution.
"""

import math

class Solution:
    def findComplement(self, num: int) -> int:
        num_digits = math.floor(math.log(num, 2) + 1)
        mask = (2**num_digits) - 1
        return mask ^ num