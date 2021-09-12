"""
this is interesting. I feel like I've done this before. We can convert using an algo like
 - determine how many 343s (7**3)
 - determine how many 49s (7**2)
 - determine how many 7s (7**1), etc.

There is probably a subtle complication with negative numbers but we can avoid a lot since we're just
building a string and put a `-` if it's less than 0.

The values start with 10**7... what is that in base 7? idk... that's what this problem is trying to answer!

I can learn about that later on. For now let's just start with a big power
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        p = 32
        remaining = abs(num)
        buffer = ""
        while p >= 0:
            num_times_it_fits = remaining // (7 ** p)
            if num_times_it_fits:
                buffer += str(num_times_it_fits)
                remaining -= (num_times_it_fits * (7 ** p))
            else:
                buffer += "0" if buffer else ""
            p -= 1
        return ("-" + buffer) if num < 0 else buffer