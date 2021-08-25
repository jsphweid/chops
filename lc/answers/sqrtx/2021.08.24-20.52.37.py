"""
So my first working solution was naive because it started at 0 and went up until finding
the best fit number. A better solution should be to start at the highest number and work downward.
This should work better for completely random numbers between 0 and 2^31-1.

The first problem with finding that number is that the number is the sqrt of the max number
i.e. the very thing we're trying to solve. Maybe we can use powers of 2 to find it?

2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
2^7 = 128
2^8 = 256

An interesting property I can spot:
- sqrt(2^8) = 2^4
- sqrt(2^6) = 2^3
- sqrt(2^4) = 2^2
- sqrt(2^2) = 2^1

But how does that work with odd numbers?
- sqrt(2^9) = 2^4.5?
    - sqrt(512) => 22 (2^4 = 16, 2^5 = 32) (hmm... 16+32/2 - 1) => 23
- sqrt(2^7) = 2^3.5?
    - sqrt(128) => 11 (2^3 = 8, 2^4 = 16) (hmm... 8+16/2 - 1) => 11
- sqrt(2^5) = 2^2.5? 
    - sqrt(32) => 5 (2^2 = 4, 2^3 = 8) (hmm... 4+8/2 - 1) => 5
I don't quite have the pattern figured out...
But I think in the case of odd number powers (which 2^31 is), it's safe
to divide by 2 and add 1 for to the power for a starting high number, then descend

It's not optimal for this method, but it should be better than starting from 0.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # actually... are we even supposed to be allowed to do this?
        start = 2 ** 16 # 16 is half of 31 + 1 rounded up

        while start >= 0:
            if start * start <= x:
                break
            start = start - 1

        return start

"""
Reflection on why it's better to start from the top for even distribution of randomness...

The nature of exponentials is that moving around in high numbers covers much more of the
space compared to lower numbers. For example, going from 10**2 to 9**2 is 100 to 81,
covering 19 numbers.

Going from 5**2 to 4**2 is 25 to 16, only 9 numbers. And 3**2 to 2**2 is 9 to 4, only 5
numbers.

It follows that you get more "bang for your buck" if you start with the large numbers
and go down because each cycle in the `while` loop above covers so much more ground
for the comparison.
"""
        
