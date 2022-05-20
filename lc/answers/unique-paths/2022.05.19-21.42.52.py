"""
===== Initial Thoughts =====
wanted to try the math approach now that I more firmly understand permutations and combinations

we already know it's just a matter of 'how many ways' can we have ddrr
ddrr
drrd
drdr
rrdd
rddr
rdrd

This was originally hard for me to think about in terms of "does order matter" and "are there repeats"

it's tempting to think of it in terms of "order does matter" and "no repeats"
if you look at it in terms of "d", you'd basically have a 4 choose 2 situation.
4*3 => 12
But we know the answer is 6. So it's not accurate. You could of course divide out
the 2*1 and bring it to 6, but what's the justification for this. That would mean
they are combinations not permutations.

Well the way I like to think of it is like lottery numbers.

Imagine you have 4 lottery numbers, 1 2 3 4
We're essentially choosing two lottery numbers
so if I choose 1 and 3, that's the same as 3 and 1. Just like drdr and drdr are the same
"""
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_d = m - 1
        num_r = n - 1
        total = num_d + num_r

        # n! / (r! * (n - r)!)
        n = total
        r = num_d
        fac = math.factorial
        return int(fac(n) / (fac(r) * fac(n - r)))
