"""
So this is a bit tricky. We could manually shift everything over one by one, then ORing it with some value

So reversing a 4 bit num 1011 would look like
result = 0
(((1011 >> 0) & 1) << 3) | result
(((1011 >> 1) & 1) << 2) | result
(((1011 >> 2) & 1) << 1) | result
(((1011 >> 3) & 1) << 0) | result

It seems like a lot of work to do for such a simple thing, but should be fine as a first pass.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (((n >> i) & 1) << (31 - i)) | result
        return result