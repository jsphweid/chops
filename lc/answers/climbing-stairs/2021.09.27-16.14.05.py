"""
===== Initial Thoughts =====
I think there is a simple pattern for this one. I think I figured it out last time. But this
is kind of an interesting DP problem potentially. I might try to solve it that way.

So if you draw the graphs, it's obviously a fibonacci sequence.

=== Brute Force Approach ===
a brute force fibonacci sequence approach, i.e. maybe a recursive implementation

~~Complexity Analysis
Time - O(2**n)
Space - O(n) - depth?

=== Implemented Approach ===
brute force with caching... i.e. dynamic programming

~~Complexity Analysis
Time - O(n)?
Space - O(n)?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def recurse(num):
            if num in cache:
                return cache[num]
            if num < 4:
                return num
            result = recurse(num - 1) + recurse(num - 2)
            cache[num] = result
            return cache[num]
        return recurse(n)

