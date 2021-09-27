"""
===== Initial Thoughts =====
I forgot how I solved it last time, but binary search should work well.

=== Brute Force Approach ===
We could simply check every number up to 2**31 and return the first number that
goes over then subtract 1.

~~Complexity Analysis
Time - O(sqrt(n)) (most is 65536 units of operation)
Space - O(1)

=== Implemented Approach ===
use binary search to find the correct number. We can use binary search because we're only
searching through integer space (and int space is sorted obviously)

Unfortunately I had to look up the answer to figure out the specific details of the binary search.
The trick here is that we needed to adjust right -1 and left +1 as well as left <= right... I got
close to that but for some reason didn't nail it.

~~Complexity Analysis
Time - O(log(sqrt(n), 2)) at most like 15 operations
Space - O(1)
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # 46341 ** 2 is max number
        left, right = 0, 46341
        while left <= right:
            midpoint = (left + right) // 2
            num = midpoint ** 2
            if x > num:
                left = midpoint + 1
            elif num > x:
                right = midpoint - 1
            else:
                return midpoint
        return right
